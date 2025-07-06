# 🧑‍💼 Face Match App

This Flask app lets users upload an ID card and a selfie to compare the faces using `face_recognition`.

## Features
- Upload ID and selfie
- Face verification
- Result display with previews
- Clean UI with Bootstrap
- Session-based results (clears on "Clear" button)

## Setup

```bash
git clone https://github.com/yourusername/face-match-app.git
cd face-match-app
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
flask --app app.py run
