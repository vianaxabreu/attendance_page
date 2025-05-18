# Student Attendance Tracker with GitHub Authentication

## 📘 Project Overview

A web-based attendance system designed to automate and simplify student attendance collection using **GitHub login**, **QR codes**, and **Google Sheets integration**.

---

## ❓ Problem Statement

Traditional attendance methods are inefficient, error-prone, and tedious.

This project provides a **digital solution** where students authenticate with their **GitHub accounts**, and their attendance is logged automatically into a **Google Sheet**, complete with timestamps and session identifiers.

---

## 🏗️ Solution Architecture

### 🔐 Authentication
Students securely authenticate via **GitHub OAuth**, ensuring verified identities without extra accounts or passwords.

### 🌐 Frontend
A minimal, responsive web interface hosted on **GitHub Pages** enables students to log in and mark attendance quickly.

### ⚙️ Backend
Developed with **Flask (Python)** and deployed on **Google Cloud Run** for scalable and reliable backend services.

### 📄 Data Logging
On successful login, the following data is recorded in a Google Sheet:
- GitHub Username
- Timestamp
- QR Session Code

### 🔲 QR Code Integration
A unique QR code is generated per session. Scanning this code initiates the login process and attaches a session-specific identifier to the attendance log.

---

## ✅ Current Status

The project is **actively under development**. Core features like GitHub login, attendance logging, and QR code flow are functional.

### In Progress:
- Enhanced session management
- User interface improvements
- Additional security layers

---

## 🛠️ Tech Stack

| Layer            | Technology                         |
|------------------|-------------------------------------|
| **Frontend**     | HTML, CSS, JavaScript, GitHub Pages |
| **Backend**      | Python (Flask), Google Cloud Run    |
| **Authentication** | GitHub OAuth                     |
| **Data Storage** | Google Sheets API                  |
| **Extras**       | QR Code generation & scanning       |

---

> _This project is part of an ongoing effort to modernize attendance tracking through automation and cloud-based technologies._