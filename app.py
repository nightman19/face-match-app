from flask import Flask, render_template, request, redirect, url_for, session
import face_recognition
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'      # Required for session

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def compare_faces(id_path, selfie_path):
    try:
        id_image = face_recognition.load_image_file(id_path)
        id_encodings = face_recognition.face_encodings(id_image)
        if not id_encodings:
            return "❌ No face found in ID image."

        selfie_image = face_recognition.load_image_file(selfie_path)
        selfie_encodings = face_recognition.face_encodings(selfie_image)
        if not selfie_encodings:
            return "❌ No face found in selfie image."

        match = face_recognition.compare_faces([id_encodings[0]], selfie_encodings[0])[0]
        return "✅ Face Match!" if match else "❌ Faces do not match."

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
