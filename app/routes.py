from flask import Blueprint, render_template, request, redirect, url_for, session, current_app, flash
import os
from werkzeug.utils import secure_filename
from .utils import compare_faces
from app.models import Verification
from app import db

main = Blueprint('main', __name__)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    id_path = None
    selfie_path = None

    if request.method == 'POST':
        id_file = request.files.get('id_image')
        selfie_file = request.files.get('selfie_image')

        if not id_file or not selfie_file:
            session['result'] = "❌ Both images are required."
            return redirect(url_for('main.index'))

        if not allowed_file(id_file.filename) or not allowed_file(selfie_file.filename):
            session['result'] = "❌ Only .jpg, .jpeg, or .png files are allowed."
            return redirect(url_for('main.index'))

        # Secure filenames and extensions
        id_filename = secure_filename(id_file.filename)
        selfie_filename = secure_filename(selfie_file.filename)

        id_ext = os.path.splitext(id_filename)[1]
        selfie_ext = os.path.splitext(selfie_filename)[1]

        # Absolute path to save files
        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)

        abs_id_path = os.path.join(upload_folder, f"id{id_ext}")
        abs_selfie_path = os.path.join(upload_folder, f"selfie{selfie_ext}")

        id_file.save(abs_id_path)
        selfie_file.save(abs_selfie_path)

        # Relative paths for browser rendering
        rel_id_path = f"uploads/id{id_ext}"
        rel_selfie_path = f"uploads/selfie{selfie_ext}"

        # Perform face match
        result_data = compare_faces(abs_id_path, abs_selfie_path)
        session['result'] = result_data['message']

        # # Save to DB
        # new_verification = Verification(
        #     id_path=rel_id_path,
        #     selfie_path=rel_selfie_path,
        #     match_result=result_data['match'],
        #     distance=result_data['distance']
        # )
        # db.session.add(new_verification)
        # db.session.commit()

        # Store result and paths in session for display
        session['result'] = "✅ Match" if result_data['match'] else "❌ No Match"
        session['id_path'] = rel_id_path
        session['selfie_path'] = rel_selfie_path

        return redirect(url_for('main.index'))

    # GET request – display result if available
    result = session.pop('result', None)
    id_path = session.pop('id_path', None)
    selfie_path = session.pop('selfie_path', None)

    print("Rendering index.html with:")
    print("id_path:", id_path)
    print("selfie_path:", selfie_path)

    return render_template('index.html', result=result, id_path=id_path, selfie_path=selfie_path)


@main.route('/test-upload', methods=['POST'])
def test_upload():
    f = request.files['file']
    path = os.path.join('static', 'uploads', secure_filename(f.filename))
    f.save(path)
    return f"Saved to {path}. Exists: {os.path.exists(path)}"


@main.route('/clear')
def clear_result():
    session.pop('result', None)
    return redirect(url_for('main.index'))

@main.route('/dashboard')
def dashboard():
    from .models import Verification
    verifications = Verification.query.order_by(Verification.timestamp.desc()).all()
    return render_template('dashboard.html', verifications=verifications)

@main.route('/delete/<int:verification_id>', methods=['GET'])
def delete_verification(verification_id):
    record = Verification.query.get_or_404(verification_id)

    # Construct absolute file path
    id_abs_path = os.path.join(current_app.root_path, 'static', record.id_path)
    selfie_abs_path = os.path.join(current_app.root_path, 'static', record.selfie_path)

    # Delete image files if they exist
    if os.path.exists(id_abs_path):
        os.remove(id_abs_path)
    if os.path.exists(selfie_abs_path):
        os.remove(selfie_abs_path)

    # Delete the record from the database
    db.session.delete(record)
    db.session.commit()

    flash("Verification recors deleted successfully.", 'success')
    return redirect(url_for('main.dashboard'))
        