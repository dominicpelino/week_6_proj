from flask import Blueprint, request, jsonify
from hero_inventory.helpers import token_required
from hero_inventory.models import db, User, Hero, hero_schema, heroes_schema


api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return {'some' : 'value'}


@api.route('/heroes', methods = ['POST'])
@token_required
def create_hero(current_user_token):
    name = request.json['name']
    alias = request.json['alias']
    species = request.json['species']
    description = request.json['description']
    powers = request.json['powers']
    max_speed = request.json['max_speed']
    max_strength = request.json['max_strength']
    user_token = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")

    hero = Hero(name, alias, species, description, powers, max_speed, max_strength, user_token = user_token)

    db.session.add(hero)
    db.session.commit()

    response = hero_schema.dump(hero)
    return jsonify(response)


@api.route('/heroes', methods = ['GET'])
@token_required
def get_heroes(current_user_token):
    owner = current_user_token.token
    heroes = Hero.query.filter_by(user_token = owner).all()
    response = heroes_schema.dump(heroes)
    return jsonify(response)


@api.route('/heroes/<id>', methods =['GET'])
@token_required
def get_hero(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        hero = Hero.query.get(id)
        response = hero_schema.dump(hero)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401


@api.route('/heroes/<id>', methods =['POST', 'PUT'])
@token_required
def update_hero(current_user_token, id):
    hero = Hero.query.get(id) 

    hero.name = request.json['name']
    hero.alias = request.json['alias']
    hero.species = request.json['species']
    hero.description = request.json['description']
    hero.powers = request.json['powers']
    hero.max_speed = request.json['max_speed']
    hero.max_strength = request.json['max_strength']
    hero.user_token = current_user_token.token

    db.session.commit()
    response = hero_schema.dump(hero)
    return jsonify(response)


@api.route('/heroes/<id>', methods = ['DELETE'])
@token_required 
def delete_hero(current_user_token, id):
    hero = Hero.query.get(id)
    db.session.delete(hero)
    db.session.commit()
    response = hero_schema.dump(hero)
    return jsonify(response)
