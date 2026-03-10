# DevOps Flask CI/CD Project 🚀
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI/CD-blue)
![Flask](https://img.shields.io/badge/Flask-Python-green)
![DevOps](https://img.shields.io/badge/DevOps-Pipeline-orange)
![CI/CD Pipeline](https://github.com/Huweda/devops-flask-ci-project/actions/workflows/ci-cd.yml/badge.svg)

## 📌 Overview
End-to-end DevOps pipeline for a Flask app using Docker, GitHub Actions, Docker Hub, Kubernetes (Minikube) and Render deployment.

## 🚀 Key Features
- Containerized Flask application using Docker
- Automated CI/CD pipeline using GitHub Actions
- Docker image versioning and push to Docker Hub
- Automatic deployment to Render via deploy hook
- Kubernetes deployment using Minikube
- Horizontal Pod Autoscaling based on CPU usage
- Production-style DevOps workflow

## ⚙️ CI/CD Pipeline Architecture
```git
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
```

## ☸️ Kubernetes Architecture

The application is deployed on Kubernetes using a Deployment, exposed via a Service, and scaled automatically using Horizontal Pod Autoscaler.

```
Docker Hub Image
       │
       ▼
Kubernetes Deployment
       │
       ▼
     Pods
       │
       ▼
    Service
       │
       ▼
Horizontal Pod Autoscaler
       │
       ▼
   Scaled Pods
```

## 🛠 Tech Stack
**Application**
- Flask

**Containerization**
- Docker
- Docker Hub

**CI/CD**
- GitHub Actions

**Orchestration**
- Kubernetes
- Minikube

**Cloud Deployment**
- Render

## 📂 Project Structure
```
flask-app/
│
├── app.py                # Main Flask application
├── test_app.py           # Unit tests for the Flask application
├── requirements.txt      # Python dependencies required for the app
├── Dockerfile            # Instructions to build the Docker container image
├── .dockerignore         # Files excluded from the Docker build context
├── .env.example          # Example environment variables template
├── .gitignore            # File/Folders ignored by git completely
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions workflow for CI/CD pipeline
├── k8s
│   ├── deployment.yaml   # Defines the Kubernetes Deployment that runs the Flask application pods
│   ├── service.yaml      # Exposes the Flask application to the network via a Kubernetes Service
│   └── hpa.yaml          # Configures Horizontal Pod Autoscaler to scale pods based on CPU usage
│
└── README.md             # Project documentation
```

## Deployment
Live Application  
https://devops-flask-app-f2ox.onrender.com/

Health Check Endpoint  
https://devops-flask-app-f2ox.onrender.com/health

## Kubernetes Deployment
This application is deployed to Kubernetes using the following resources:

- Deployment
- Service
- Horizontal Pod Autoscaler

Deploy using:
kubectl apply -f k8s/

## Autoscaling

The project uses Kubernetes Horizontal Pod Autoscaler.

Configuration:
- Min Pods: 2
- Max Pods: 10
- CPU Threshold: 50%

Command used:

kubectl autoscale deployment flask-app-deployment --cpu-percent=50 --min=2 --max=10

## Quick Start

## ⚡ Quick Start

Start Minikube:

minikube start

Deploy Kubernetes resources:

kubectl apply -f k8s/

Check pods:

kubectl get pods

Access the service:

minikube service flask-app-service

## Environment Configuration

The application supports environment variables for configuration.

Example:
APP_MESSAGE=Hello from Kubernetes!

Environment variables can be configured in the Kubernetes deployment manifest.