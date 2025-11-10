# 🧑‍💼 Face Match App

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Framework-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 📸 Overview


**Face Match App** is a lightweight **Flask** web application that allows users to upload an ID card and a selfie to verify identity.

It works by comparing the two images using the `face_recognition` library, which calculates **128-dimensional face embeddings** and measures the **Euclidean distance** between them to determine a match.

All verification results are stored locally in a **SQLite database** and displayed in a clean, Bootstrap-powered dashboard with filtering options.

---

## ✨ Features

* 📤 Upload ID card and selfie for comparison
* 🧠 **Facial recognition** using the `face_recognition` library
* 📊 Dashboard with history, filtering, and pagination
* 🗃️ **SQLite** for local data persistence
* 🧹 Session-based clearing of results to maintain privacy
* 💻 Clean, responsive UI built with **Bootstrap 5**

---

## ⚙️ Installation & Setup

To get the application up and running locally, follow these steps:

```bash
# Clone the repository
git clone [https://github.com/yourusername/face-match-app.git](https://github.com/yourusername/face-match-app.git)
cd face-match-app

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
flask --app app.py run

# 🌐 Open your browser and navigate to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
````

-----

## 📂 Project Structure

This is an overview of the key files and directories:

```
face-match-app/
├── app/
│   ├── routes.py         # Handles web requests and core logic
│   ├── models.py         # Defines the database structure (SQLite)
│   ├── templates/
│   │   ├── index.html    # The main upload page
│       └── dashboard.html# The history and results page
│   └── static/
│       └── uploads/      # 📂 Stores temporary uploaded ID/selfie images
├── requirements.txt      # List of project dependencies
├── app.py                # The main Flask application entry point
└── README.md
```

-----

## 🧩 Tech Stack

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Flask (Python) | Lightweight web framework for the core application. |
| **Face Recognition** | `face_recognition` | Library used for face detection and feature comparison. |
| **Database** | SQLite | Serverless, file-based database for storing verification history. |
| **Frontend** | Bootstrap 5 | Used for a clean, responsive, and modern user interface. |
| **Language** | Python 3.10+ | The core programming language. |

-----

## 🚀 Future Improvements

  * 🔐 Implement **User Authentication** for restricted access.
  * ☁️ Integrate **Cloud Storage** (e.g., S3) for persistent image storage.
  * 🧱 Add **Docker** support for easy containerized deployment.
  * 🧾 Create **REST API endpoints** for external system integrations.

-----

## 👨‍💻 Author

**Nuru Mohammed**

  * 💼 [LinkedIn](https://linkedin.com/in/yourprofile)
  * 📧 [your.email@example.com](mailto:your.email@example.com)
  * 🌍 [GitHub Profile](https://github.com/yourusername)

-----

## 📜 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it.

-----

> ⚡ *“Not every web app needs Django. Sometimes, Flask + clean architecture does the job beautifully.”*

```

Now that your project's documentation is finalized, would you like to start working on a specific file, such as `app.py`, `models.py`, or `routes.py`, to implement the core logic?
```