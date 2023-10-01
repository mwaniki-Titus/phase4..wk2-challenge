from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_only=('id', 'name', 'super_name', 'powers')
    serialize_rules= ('-powers.heroes',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    powers = db.relationship('Power', secondary='hero_powers', back_populates='heroes')

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    serialize_only=('id', 'name', 'description')
    serialize_rules=('-heroes.powers',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    heroes = db.relationship('Hero', secondary='hero_powers', back_populates='powers')

    @validates('description')
    def validates_description(self, key, description):
        if not description:
            raise ValueError("Description field cannot be empty.")
        elif(len(description)< 20):
            raise ValueError("Description must contain at least 20 characters.")
        else:
            return description
