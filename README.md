# Project-List-Management-App
Scalable Project Management Web App | Flask + PostgreSQL + AWS EC2

# 📊 Scalable Project Management Web App

A responsive and scalable project management web application built with **Flask**, **PostgreSQL**, and hosted on **AWS EC2**. This tool allows users to organize and track tasks across multiple categories, export reports as PDFs, and manage their workflow with an intuitive interface.

---

## 🚀 Features

- **🖥 Responsive UI**  
  Built with HTML, Bootstrap, and Font Awesome for smooth performance on desktop, tablet, and mobile devices.

- **📁 Project & Task Management**  
  Categorize projects into sections such as *Home*, *Work*, and *Events & Lifestyle*. Add, update, and track tasks within each project.

- **🔄 Dynamic Data Interaction**  
  Create and delete projects and tasks with real-time feedback via Flask flash messaging.

- **🔐 Backend with Flask & PostgreSQL**  
  - Flask-SQLAlchemy models with cascading deletes  
  - Secure input validation and efficient query handling  
  - Remote PostgreSQL database hosted on AWS

- **☁️ Cloud Deployment**  
  - Hosted on AWS EC2 for performance and scalability  
  - Environment variables managed with `.env` for secure config

---

## 🛠️ Tech Stack

| Layer        | Technologies Used                          |
|--------------|---------------------------------------------|
| **Frontend** | HTML, CSS, Bootstrap, Font Awesome          |
| **Backend**  | Python, Flask, Flask-SQLAlchemy             |
| **Database** | PostgreSQL (hosted on AWS)                  |
| **Cloud**    | AWS EC2                                     |
| **PDF Export**| wkhtmltopdf, pdfkit                        |
| **Dev Tools**| Git, GitHub, Python-dotenv (`.env`)         |

---

## 📂 Project Structure

```bash
project-management-app/
│
├── static/                 # CSS and images
├── templates/              # HTML templates (Jinja2)
├── app.py                  # Main Flask application
├── models.py               # SQLAlchemy models
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (DB URI, secret key)
└── README.md               # Project documentation

