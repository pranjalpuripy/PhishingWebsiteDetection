# 🛡️ CyberShield AI

### AI-Based Phishing Website Detection System

CyberShield AI is a Machine Learning based web application designed to detect potentially phishing websites by analyzing the URL submitted by a user.

The system uses a trained Machine Learning model to classify a website as either **SAFE** or **PHISHING** and stores the scan results for future reference.

---

## 📌 Project Overview

Phishing is one of the most common cybersecurity threats where attackers create fake websites to steal sensitive information such as usernames, passwords, banking details and other personal data.

CyberShield AI provides a simple and user-friendly platform where users can enter a website URL and check its security status.

The application combines:

- Machine Learning
- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

to create a complete web-based phishing detection system.

---

## 🎯 Project Objective

The main objectives of CyberShield AI are:

- To detect potentially phishing websites using Machine Learning.
- To provide a simple URL scanning interface.
- To classify submitted URLs as Safe or Phishing.
- To maintain a history of scanned websites.
- To provide dashboard statistics for scan activity.
- To demonstrate the practical use of Machine Learning in cybersecurity.

---

## ✨ Key Features

### 🔐 User Authentication

- User registration
- User login
- Session-based authentication
- Logout functionality
- Protected application pages

### 🔎 AI-Based URL Scanning

- Enter a website URL
- Analyze the URL using a trained Machine Learning model
- Display the detection result
- Show Safe or Phishing status

### 📊 Dashboard

The dashboard provides:

- Total number of scans
- Total safe websites
- Total phishing websites
- Today's scan count
- Recent scan activity
- Quick access to major system features

### 📋 Scan History

The system stores scanned URLs in the SQLite database and displays:

- Website URL
- Detection result
- Scan date and time

### ℹ️ About Page

The About section provides information about:

- Project overview
- How the system works
- Technologies used
- Key features
- Project objective

### 🎨 User Interface

- Clean and modern interface
- Responsive design
- Easy navigation
- Security-focused visual design

---

## ⚙️ How the System Works

```text
                User
                  │
                  ▼
          Enter Website URL
                  │
                  ▼
          URL Preprocessing
                  │
                  ▼
       Feature / Text Processing
                  │
                  ▼
        Machine Learning Model
                  │
          ┌───────┴───────┐
          ▼               ▼
        SAFE           PHISHING
          │               │
          └───────┬───────┘
                  ▼
          Display Result
                  │
                  ▼
          Save Scan History
                  │
                  ▼
             Dashboard

🧠 Machine Learning

The project uses a trained Machine Learning model to classify URLs.

The URL is converted into a numerical representation using a vectorizer and then passed to the trained classification model.

Prediction
Prediction = 0  →  SAFE

Prediction = 1  →  PHISHING

The trained model and vectorizer are stored inside the model/ directory.

Note: This project is an educational prototype. Its detection accuracy depends on the dataset and trained model and should not be considered a production-grade cybersecurity solution.

🛠️ Technologies Used
Technology	Purpose
Python	Backend programming
Flask	Web application framework
HTML5	Web page structure
CSS3	User interface and styling
JavaScript	Client-side functionality
SQLite	Database
Scikit-learn	Machine Learning
Pandas	Dataset processing
Joblib	Saving and loading ML models
📁 Project Structure
PhishingWebsiteDetection/
│
├── app.py
├── README.md
├── requirements.txt
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── database.db
│
├── dataset/
│   └── phishing_dataset.csv
│
├── model/
│   ├── feature_extraction.py
│   ├── phishing_model.pkl
│   ├── train_model.py
│   └── vectorizer.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── images/
│   │   ├── logo.png
│   │   ├── shield.png
│   │   └── warning.png
│   │
│   └── js/
│       └── script.js
│
└── templates/
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── scan.html
    ├── result.html
    ├── history.html
    └── about.html
💻 Installation and Setup
1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>

Move into the project directory:

cd PhishingWebsiteDetection
2. Create a Virtual Environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
3. Install Required Packages
pip install -r requirements.txt
4. Run the Application
python app.py

The application will start locally.

Open the following URL in your browser:

http://127.0.0.1:5000
🔑 Application Flow
Home Page
    ↓
Register
    ↓
Login
    ↓
Dashboard
    ↓
Scan URL
    ↓
AI Detection
    ↓
Result
    ↓
Scan History
📊 Dashboard Features

The dashboard dynamically displays:

Total Scans
Safe Websites
Phishing Websites
Today's Scans
Recent Scan Activity

The statistics are retrieved from the SQLite database.

🗄️ Database

The application uses SQLite for storing application data.

Users Table

Stores:

User ID
Full Name
Email
Password
Scan History Table

Stores:

Scan ID
Website URL
Detection Result
Scan Date
🔒 Security Considerations

This project is developed primarily for educational and demonstration purposes.

For a production system, additional security measures should be implemented, including:

Password hashing
Secure environment variables
Strong secret key management
CSRF protection
HTTPS
Input sanitization
More comprehensive phishing datasets
Regular Machine Learning model updates
🚀 Future Enhancements

Possible future improvements include:

Advanced URL feature extraction
Larger real-world phishing datasets
Improved Machine Learning models
Website screenshot analysis
Real-time threat intelligence
URL reputation checking
Email phishing detection
Admin dashboard
User-specific scan history
Improved security and password hashing
🎓 Project Type

Academic / Educational Project

This project demonstrates the integration of:

Machine Learning
        +
Cybersecurity
        +
Web Development
        +
Database Management
👨‍💻 Developer

Pranjal Puri

BCA Student

📜 Disclaimer

CyberShield AI is an educational project created to demonstrate phishing website detection using Machine Learning.

The predictions generated by the system should not be treated as guaranteed security assessments. Users should always verify website URLs and avoid entering sensitive information on suspicious websites.

⭐ Acknowledgement

This project was developed as part of an academic project to explore the practical application of Machine Learning and web technologies in the field of cybersecurity.


## Step 2 — One important change before saving

In this line:

```markdown
git clone <YOUR_GITHUB_REPOSITORY_URL>