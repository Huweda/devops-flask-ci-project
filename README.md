# DevOps Flask CI/CD Project 🚀

## 📌 Overview
This project demonstrates containerization of a Python Flask application using Docker and CI automation using GitHub Actions.

## 🛠 Tech Stack
- Python (Flask)
- Docker
- Git
- GitHub Actions
- Linux

## 🚀 Features
- Dockerized application
- Environment variable configuration
- Health check endpoint
- Automated CI pipeline on push

## ▶️ Run Locally

Build the image:
docker build -t devops-flask-app .

Run the container:
docker run -d -p 5000:5000 -e ENVIRONMENT=dev devops-flask-app

Access in browser:
http://localhost:5000
