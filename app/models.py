from . import db
from datetime import datetime, timezone


class Verification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_path = db.Column(db.String(120), nullable=False)
    selfie_path = db.Column(db.String(120), nullable=False)
    match_result = db.Column(db.Boolean, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))