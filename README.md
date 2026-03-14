# Cloud Log Monitoring and Alert System

## 📌 Overview

The **Cloud Log Monitoring and Alert System** is a lightweight monitoring tool that analyzes application log files, detects severity levels, and sends alerts when critical issues occur.
It provides a simple dashboard to visualize log statistics and helps developers identify system problems quickly.

This project demonstrates concepts used in real-world monitoring tools such as log analysis, alerting, and dashboard visualization.

---

## 🚀 Features

* Upload and analyze application log files
* Detect log severity levels:

  * INFO
  * WARNING
  * ERROR
  * CRITICAL
* Automated email alerts for critical issues
* REST API for log monitoring
* Web dashboard to display log statistics
* Cloud deployment with separate backend and frontend services

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Tools & Services

* Mailtrap (Email Testing)
* Render (Backend Deployment)
* Vercel (Frontend Hosting)

---

## 🏗 Project Architecture

Frontend (Dashboard)
⬇
Backend API (FastAPI)
⬇
Log Processing & Alert System

Logs are uploaded through the API, analyzed for severity levels, and the results are displayed on the dashboard. If critical issues are detected, an alert email is triggered.

---

## 📂 Project Structure

```
Cloud-log-monitoring-and-alert-system
│
├── main.py
├── log_analyzer.py
├── email_alert.py
│
├── frontend
│   └── index.html
│
├── sample_log.txt
├── sample_norm.txt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/Vishnuvardhan-Ande/Cloud-log-monitoring-and-alert-system.git
cd Cloud-log-monitoring-and-alert-system
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Backend

Start the FastAPI server:

```
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Using the Dashboard

1. Start the backend server
2. Upload a sample log file using `/upload-log`
3. Open the frontend dashboard
4. Click **Refresh Logs** to view analysis results

The dashboard displays the count of:

* INFO logs
* WARNING logs
* ERROR logs
* CRITICAL logs

---

## 📧 Email Alerts

When the system detects **ERROR or CRITICAL logs**, an alert email is sent using Mailtrap.

This helps simulate real-world alert systems used in production environments.

---

## 🌐 Live Demo

Frontend Dashboard

```
https://cloud-log-monitoring-and-alert-syst.vercel.app/
```

Backend API

```
https://cloud-log-monitoring-and-alert-system.onrender.com/docs
```

---

## 🎯 Use Cases

* Monitoring application logs
* Detecting system failures early
* DevOps log analysis
* Learning cloud monitoring architecture

---

## ⭐ If you like this project

Give it a star on GitHub!
