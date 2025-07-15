# 🐍 Python Log Analyzer with Docker & Jenkins

A simple DevOps mini project that demonstrates CI/CD using **Python**, **Docker**, **Jenkins**, **GitHub**, and **Linux**.

---

## 📌 Project Overview

This project contains a Python script (`analyzer.py`) that reads a system log file and counts the number of lines with:
- `INFO`
- `WARNING`
- `ERROR`

The project is:
- Containerized using Docker
- Connected to Jenkins for automated CI/CD
- Fully executable in a Linux environment via shell scripting

---

## 🧰 Tech Stack

- 🐍 Python 3.9
- 🐳 Docker
- 🧪 Jenkins
- 🐧 Linux Shell Script
- 🌐 Git & GitHub

---

## 📁 Project Structure

python-log-analyzer/
├── analyzer.py # Python script to analyze logs
├── logs.txt # Sample log file
├── Dockerfile # Docker build configuration
├── requirements.txt # Python dependencies


---

## 🐳 Docker Instructions

### 🔧 Build the Docker image

```bash
docker build -t log-analyzer .


▶️ Run the Docker container
bash```
docker run --rm log-analyzer

Output:

Total Lines: 3
INFO: 1, WARNING: 1, ERROR: 1


📸 Sample Output

Total Lines: 3
INFO: 1
WARNING: 1
ERROR: 1