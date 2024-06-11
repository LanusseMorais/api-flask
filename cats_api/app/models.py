from app import db

class CatBreed(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    origin = db.Column(db.String)
    temperament = db.Column(db.String)
    description = db.Column(db.String)

class CatImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breed_id = db.Column(db.String, db.ForeignKey('cat_breed.id'), nullable=False)
    url = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)  # chapéu ou óculos
