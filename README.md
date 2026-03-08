# DevOps Flask CI/CD Project 🚀
![CI/CD Pipeline](https://github.com/Huweda/devops-flask-ci-project/actions/workflows/ci-cd.yml/badge.svg)

## 📌 Overview
A simple Flask application demonstrating a complete CI/CD pipeline using Docker, GitHub Actions, Docker Hub, and Render.

## 🛠 Tech Stack
- Flask
- Docker
- GitHub Actions
- Docker Hub
- Render

## ⚙️ CI/CD Pipeline Architecture
Developer
   │
   ▼
GitHub Repository
   │
   ▼
GitHub Actions (CI Pipeline)
   │
   ├─ Run Tests
   ├─ Build Docker Image
   └─ Push Image → Docker Hub
   │
   ▼
Render Deploy Hook
   │
   ▼
Render Cloud Platform
   │
   ▼
Live Flask Application

## 📂 Project Structure

devops-flask-ci-project/
│
├── app.py                # Main Flask application
├── test_app.py           # Unit tests for the Flask application
├── requirements.txt      # Python dependencies required for the app
├── Dockerfile            # Instructions to build the Docker container image
├── .dockerignore         # Files excluded from the Docker build context
├── .env.example          # Example environment variables template
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions workflow for CI/CD pipeline
│
└── README.md             # Project documentation

## Deployment
Live Application  
https://devops-flask-app-f2ox.onrender.com/

Health Check Endpoint  
https://devops-flask-app-f2ox.onrender.com/health

## 🚀 Features
- Containerized Flask application using Docker
- Automated CI/CD pipeline using GitHub Actions
- Docker image versioning and push to Docker Hub
- Automatic deployment to Render via deploy hook
