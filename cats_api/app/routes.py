from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.models import CatBreed, CatImage

bp = Blueprint('api', __name__)

@bp.route('/breeds', methods=['GET'])
@swag_from('swagger/get_breeds.yml')
def get_breeds():
    breeds = CatBreed.query.all()
    return jsonify([breed.name for breed in breeds])

@bp.route('/breeds/<breed_id>', methods=['GET'])
@swag_from('swagger/get_breed_info.yml')
def get_breed_info(breed_id):
    breed = CatBreed.query.get_or_404(breed_id)
    images = CatImage.query.filter_by(breed_id=breed_id).all()
    return jsonify({
        'name': breed.name,
        'origin': breed.origin,
        'temperament': breed.temperament,
        'description': breed.description,
        'images': [img.url for img in images]
    })

@bp.route('/breeds/temperament/<temperament>', methods=['GET'])
@swag_from('swagger/get_breeds_by_temperament.yml')
def get_breeds_by_temperament(temperament):
    breeds = CatBreed.query.filter(CatBreed.temperament.ilike(f"%{temperament}%")).all()
    return jsonify([breed.name for breed in breeds])

@bp.route('/breeds/origin/<origin>', methods=['GET'])
@swag_from('swagger/get_breeds_by_origin.yml')
def get_breeds_by_origin(origin):
    breeds = CatBreed.query.filter(CatBreed.origin.ilike(f"%{origin}%")).all()
    return jsonify([breed.name for breed in breeds])
