from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Devops Journey Started 🚀"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/env")
def env():
    return {"environment": os.getenv("ENVIRONMENT", "not set")}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)