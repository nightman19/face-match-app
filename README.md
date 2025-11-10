# 🧑‍💼 Face Match App

A lightweight **Flask** application that allows users to upload an ID card and a selfie to verify identity by comparing the two images using the `face_recognition` library.  
Results are logged in a local **SQLite database** and visualized through a clean, responsive dashboard.

---

## ✨ Features

- 📤 Upload ID card and selfie for comparison  
- 🧠 Automatic face matching using `face_recognition`  
- 📊 Dashboard with verification history and filtering options  
- 🗃️ Data stored locally with SQLite  
- 🧹 Session-based result clearing  
- 💻 Simple and clean Bootstrap-based UI  

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/face-match-app.git
cd face-match-app

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
flask --app app.py run

```
## 📂 Project Structure

```bash
face-match-app/
├── app/
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   └── static/
│       └── uploads/
├── requirements.txt
├── app.py
└── README.md
```
## 🧩 Tech Stack