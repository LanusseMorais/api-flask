import requests
from app import db
from app.models import CatBreed, CatImage
from config import Config

def fetch_and_store_cat_data():
    headers = {'x-api-key': Config.CAT_API_KEY}
    response = requests.get(f"{Config.CAT_API_URL}/breeds", headers=headers)
    breeds = response.json()

    for breed in breeds:
        breed_id = breed.get('id')
        name = breed.get('name')
        origin = breed.get('origin')
        temperament = breed.get('temperament')
        description = breed.get('description')
        
        cat_breed = CatBreed(id=breed_id, name=name, origin=origin, temperament=temperament, description=description)
        db.session.add(cat_breed)

        images_response = requests.get(f"{Config.CAT_API_URL}/images/search?breed_id={breed_id}&limit=3", headers=headers)
        images = images_response.json()
        for img in images:
            cat_image = CatImage(breed_id=breed_id, url=img.get('url'), category='breed')
            db.session.add(cat_image)

    categories = ['hats', 'sunglasses']
    for category in categories:
        images_response = requests.get(f"{Config.CAT_API_URL}/images/search?category_ids={category}&limit=3", headers=headers)
        images = images_response.json()
        for img in images:
            cat_image = CatImage(breed_id=None, url=img.get('url'), category=category)
            db.session.add(cat_image)

    db.session.commit()
