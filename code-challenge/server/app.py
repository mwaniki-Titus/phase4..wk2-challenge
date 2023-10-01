#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hero, Power, Hero_power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return 'Welcome to SuperHeroes Api!'

class Heroes(Resource):
    
    def get(self):
        hero_dict = [hero.to_dict() for hero in Hero.query.all()]
        return make_response(jsonify(hero_dict), 200)
    
api.add_resource(Heroes, '/heroes')

class HeroesById(Resource):
    
    def get(self, id):
        hero_id = [hero.id for hero in Hero.query.all()]
        if(id in hero_id):
            hero_dict = Hero.query.filter_by(id = id).first().to_dict()
            return make_response(jsonify(hero_dict), 200)
        else:
            return {"error": "Hero not found"}
    
api.add_resource(HeroesById, '/heroes/<int:id>')

class Powers(Resource):
    
    def get(self):
        power_dict = [power.to_dict() for power in Power.query.all()]
        return make_response(jsonify(power_dict), 200)
    
api.add_resource(Powers, '/powers')

class PowersById(Resource):
    
    def get(self, id):
        power_id = [power.id for power in Power.query.all()]
        if(id in power_id):
            power_dict = Power.query.filter_by(id = id).first().to_dict()
            return make_response(jsonify(power_dict), 200)
        else:
            return {"error": "Power not found"}
        
    def patch(self, id):
        power_id = [power.id for power in Power.query.all()]
        if(id in power_id):
            power = Power.query.filter_by(id = id).first()
            for attr in request.form:
                setattr(power, attr, request.form[attr])

            db.session.add(power)
            db.session.commit()

            response_dict = power.to_dict()

            return make_response(response_dict,200)
        else:
            return {"error": "Power not found"}
    
api.add_resource(PowersById, '/powers/<int:id>')

class HeroPowers(Resource):
    def post(self):
        data = request.form
        new_record = Hero_power(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id'],
        )

        db.session.add(new_record)
        db.session.commit()

        response_dict = new_record.to_dict()

        return make_response(response_dict ,200)
    
api.add_resource(HeroPowers, '/hero_powers')

if __name__ == '__main__':
    app.run(port=5555)