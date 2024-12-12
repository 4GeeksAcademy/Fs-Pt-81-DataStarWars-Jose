import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # Nombre de la tabla en plural
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    favoritos = relationship("Favorito")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }

class Character(Base):
    __tablename__ = 'characters'  # Nombre de la tabla en plural
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    height = Column(String, nullable=False)
    mass = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    homeworld = Column(String, nullable=False)
    films = Column(String, nullable=False)

    favoritos = relationship("Favorito")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "films": self.films
        }

class Planet(Base):
    __tablename__ = 'planets'  # Nombre de la tabla en plural
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rotation_period = Column(String, nullable=False)
    orbital_period = Column(String, nullable=False)
    diameter = Column(String, nullable=False)
    climate = Column(String, nullable=False)
    gravity = Column(String, nullable=False)
    surface_water = Column(String, nullable=False)
    population = Column(String, nullable=False)
    residents = Column(String, nullable=False)

    favoritos = relationship("Favorito")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "surface_water": self.surface_water,
            "population": self.population,
            "residents": self.residents
        }

class Vehicle(Base):
    __tablename__ = 'vehicles'  # Nombre de la tabla en plural
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    manufacture = Column(String, nullable=False)
    cost_in_credits = Column(String, nullable=False)
    length = Column(String, nullable=False)
    max_atmosphering_speed = Column(String, nullable=False)
    crew = Column(String, nullable=False)
    passengers = Column(String, nullable=False)
    cargo_capacity = Column(String, nullable=False)
    consumables = Column(String, nullable=False)
    hyperdrive_rating = Column(String, nullable=False)
    MGLT = Column(String, nullable=False)
    starship_class = Column(String, nullable=False)
    pilots = Column(String, nullable=False)
    films = Column(String, nullable=False)

    favoritos = relationship("Favorito")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacture": self.manufacture,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "starship_class": self.starship_class,
            "pilots": self.pilots,
            "films": self.films
        }

class Favorito(Base):
    __tablename__ = 'favoritos'  # Nombre de la tabla en plural
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)

    user = relationship("User")
    character = relationship("Character")
    planet = relationship("Planet")
    vehicle = relationship("Vehicle")


# Draw the ER diagram from SQLAlchemy base
render_er(Base, 'diagram.png')
