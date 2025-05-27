from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)
# Load environment variables from .env file
load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db=SQLAlchemy(app)

class Container(db.Model):
    __tablename__ = "containers"
    container_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    

    # Relationship: One container can have multiple projects
    projects = db.relationship("Project", back_populates="container", cascade="all, delete-orphan")


class Project(db.Model):
    __tablename__ = "projects"
    project_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(length = 50))
    
    # Foreign key: Links each project to a container
    container_id = db.Column(db.Integer, db.ForeignKey('containers.container_id'), nullable=True)
    # Relationship: Each project belongs to one container
    container = db.relationship("Container", back_populates="projects")

    task = db.relationship("Task", back_populates = "project", cascade = "all, delete-orphan")

class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key = True)
    project_id= db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    description = db.Column(db.String(length=50))

    project = db.relationship("Project", back_populates ="task")


# Define app routes
@app.route("/")
def show_projects():
    return render_template('index.html', projects=Project.query.all())


@app.route("/project/<project_id>")
def show_tasks(project_id):
    return render_template('project-tasks.html', 
                           project= Project.query.filter_by(project_id=project_id).first(),
                           tasks= Task.query.filter_by(project_id=project_id).all())


@app.route("/add/project", methods=['POST'])
def add_project():
    #TO DO: Add Project
    if not request.form['project-title']:
        flash('Enter a title for your new project', 'red')
    else:
        project = Project(title=request.form['project-title'])
        db.session.add(project)
        db.session.commit()
        flash("Project added successfully", "green")

    return redirect(url_for('show_projects'))

@app.route("/add/project/containers/<container_id>", methods=['POST'])
def add_project_to_container(container_id, project_title):
    container = Container.query.get(container_id)
    if container:
        new_project = Project(title=project_title, container_id=container_id)
        db.session.add(new_project)
        db.session.commit()
        print(f"Project '{project_title}' added to container '{container.name}'.")
    else:
        print("Container not found.")
    return redirect(url_for('show_tasks'))

@app.route("/add/task/<project_id>", methods=['POST'])
def add_task(project_id):
    print("Received POST request for task")
    if not request.form['task-name']:
        flash('Enter a description for your new task', 'red')
    else:
        task = Task(description=request.form['task-name'], project_id=project_id)
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully', 'green')
    return redirect(url_for('show_tasks', project_id=project_id))

@app.route('/delete/task/<task_id>', methods=['POST'])
def delete_task(task_id):
    pending_delete_task = Task.query.filter_by(task_id=task_id).first()
    original_project_id = pending_delete_task.project.project_id
    db.session.delete(pending_delete_task)
    db.session.commit()
    return redirect(url_for('show_tasks', project_id = original_project_id))

@app.route('/delete/project/<project_id>', methods=['POST'])
def delete_project(project_id):
    pending_delete_project = Project.query.filter_by(project_id =project_id).first()
    db.session.delete(pending_delete_project)
    db.session.commit()
    return redirect(url_for('show_projects'))


if __name__ == '__main__':
    app.run(debug=True)



