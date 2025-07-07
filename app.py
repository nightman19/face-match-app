from flask import Flask, render_template, request, redirect, url_for, session
import face_recognition
from face_recognition import face_distance
import os

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db, Verification 


app = Flask(__name__)
app.secret_key = 'your-secret-key'      # Required for session

# Alchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///verifications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Verification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_path = db.Column(db.String(120), nullable=False)
    selfie_path = db.Column(db.String(120), nullable=False)
    match_result = db.Column(db.Boolean, nullable=False)
    distance = db.Column(db.Float, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def compare_faces(id_path, selfie_path):
    try:
        id_image = face_recognition.load_image_file(id_path)
        id_encodings = face_recognition.face_encodings(id_image)
        if len(id_encodings) != 1:
            return "❌ No face or multiple faces found in ID image."

        selfie_image = face_recognition.load_image_file(selfie_path)
        selfie_encodings = face_recognition.face_encodings(selfie_image)
        if len(selfie_encodings) != 1:
            return "❌ No face or multiple faces found in selfie image."

        id_encoding = id_encodings[0]
        selfie_encoding = selfie_encodings[0]

        # Compute face distance and apply custom threshold
        distance = face_recognition.face_distance([id_encoding], selfie_encoding)[0]
        print(f"[DEBUG] Face distance: {distance}")  # Optional: Remove in production

        # Use a stricter threshold (e.g., 0.45 or even 0.40)
        is_match = distance < 0.45

        # Save to database
        record = Verification(
            id_path=id_path,
            selfie_path=selfie_path,
            match_result=is_match,
            distance=round(distance, 4)
        )
        db.session.add(record)
        db.session.commit()


        return "✅ Face Match!" if is_match else f"❌ Faces do not match (Distance: {distance:.2f})"

    except Exception as e:
        return f"❌ Error: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        id_file = request.files['id_image']
        selfie_file = request.files['selfie_image']

        id_path = os.path.join(app.config['UPLOAD_FOLDER'], 'id.jpg')
        selfie_path = os.path.join(app.config['UPLOAD_FOLDER'], 'selfie.jpg')

        id_file.save(id_path)
        selfie_file.save(selfie_path)

        result = compare_faces(id_path, selfie_path)
        session['result'] = result

        return redirect(url_for('index')) 

    
     # GET request
    result = session.pop('result', None)
    return render_template('index.html', result=result)

@app.route('/clear')
def clear_result():
    session.pop('result', None)
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)
