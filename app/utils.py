import face_recognition
from .models import Verification
from . import db
import os

def compare_faces(id_path, selfie_path):
    '''This function handles the compare face logic'''

    try:
        id_image = face_recognition.load_image_file(id_path)
        id_encodings = face_recognition.face_encodings(id_image)
        if len(id_encodings) != 1:
            return {
                "message": "❌ No face or multiple faces found in ID image.",
                "match": False,
                "distance": None
            }
        
        selfie_image = face_recognition.load_image_file(selfie_path)
        selfie_encodings = face_recognition.face_encodings(selfie_image)
        if len(selfie_encodings) != 1:
            return {
                "message": "❌ No face or multiple faces found in selfie image.",
                "match": False,
                "distance": None
            }

        distance = face_recognition.face_distance([id_encodings[0]], selfie_encodings[0])[0]
        is_match = distance < 0.45

        record = Verification(
            id_path=os.path.join("uploads", os.path.basename(id_path)),
            selfie_path=os.path.join("uploads", os.path.basename(selfie_path)),
            match_result=is_match,
            distance=round(distance, 4)
        )

        db.session.add(record)
        db.session.commit()

        return {
            "message": "✅ Face Match!" if is_match else f"❌ Faces do not match (Distance: {distance:.2f})",
            "match": is_match,
            "distance": round(distance, 4)
        }
    except Exception as e:
        return {
            "message": f"❌ Error: {str(e)}",
            "match": False,
            "distance": None
        }
