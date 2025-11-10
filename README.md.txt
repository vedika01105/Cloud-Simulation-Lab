# Cloud Simulation Lab 
This project simulates a real cloud deployment using Docker and Google Colab.

## 🧠 What I Learned
- Creating and running Docker containers (`python:3.10`)
- Mounting local folders into containers
- Setting up virtual environments inside Docker
- Running Python scripts from inside containers
- Simulating cron automation using Python loops
- Managing files between local and container (`docker cp`)

## ⚙️ How to Run
1. Pull the Python image:
   ```bash
   docker pull python:3.10

2. Run a container with volume mount:
   ```bash
   docker run -it -v "path_to_your_folder:/app" -w /app python:3.10 bash

3. Activate venv and run your script:
   ```bash
   source myvenv/bin/activate
   python test_script.py

📦 Tools Used

Docker
Python 3.10
Virtual Environments
Colab (for cloud simulation)

