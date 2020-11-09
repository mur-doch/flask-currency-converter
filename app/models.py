from app import db

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acronym = db.Column(db.String(3), index=True, unique=True)
    name = db.Column(db.String(120), index=True)
    min_size = db.Column(db.Float)
    usd_value = db.Column(db.Float)
