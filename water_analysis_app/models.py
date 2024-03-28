from flask_sqlalchemy import SQLAlchemy
from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from water_analysis_app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    feedbacks = db.relationship('Feedback', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user = db.relationship('User', back_populates='feedbacks')

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    ph_level = db.Column(db.Float, nullable=False)
    conductivity = db.Column(db.Float, nullable=False)
    oxygen_level = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)

class Prediction(db.Model):
    __tablename__ = 'prediction'
    id = db.Column(db.Integer, primary_key=True)
    prediction_date = db.Column(db.DateTime, nullable=False)
    predicted_values = db.Column(db.JSON, nullable=False)

class Visualization(db.Model):
    __tablename__ = 'visualization'
    id = db.Column(db.Integer, primary_key=True)
    chart_type = db.Column(db.String(120), nullable=False)
    data_parameters = db.Column(db.JSON, nullable=False)

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True) 
    location_group = db.Column(db.String(120), nullable=False)
    site_number = db.Column(db.String(120), nullable=False)
    site_name = db.Column(db.String(120), nullable=False)
    decimal_latitude = db.Column(db.Float, nullable=False)
    decimal_longitude = db.Column(db.Float, nullable=False)

class Feature(db.Model):
    __tablename__ = 'feature'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)


class XTrain(db.Model):
    __tablename__ = 'x_train'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    feature1 = db.Column(db.Float, nullable=False)
    feature2 = db.Column(db.Float, nullable=False)
    feature3 = db.Column(db.Float, nullable=False)
    feature4 = db.Column(db.Float, nullable=False)
    feature5 = db.Column(db.Float, nullable=False)
    feature6 = db.Column(db.Float, nullable=False)
    feature7 = db.Column(db.Float, nullable=False)
    feature8 = db.Column(db.Float, nullable=False)
    feature9 = db.Column(db.Float, nullable=False)
    feature10 = db.Column(db.Float, nullable=False)
    feature11 = db.Column(db.Float, nullable=False)

class XTest(db.Model):
    __tablename__ = 'x_test'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    feature1 = db.Column(db.Float, nullable=False)
    feature2 = db.Column(db.Float, nullable=False)
    feature3 = db.Column(db.Float, nullable=False)
    feature4 = db.Column(db.Float, nullable=False)
    feature5 = db.Column(db.Float, nullable=False)
    feature6 = db.Column(db.Float, nullable=False)
    feature7 = db.Column(db.Float, nullable=False)
    feature8 = db.Column(db.Float, nullable=False)
    feature9 = db.Column(db.Float, nullable=False)
    feature10 = db.Column(db.Float, nullable=False)
    feature11 = db.Column(db.Float, nullable=False)


class YTrain(db.Model):
    __tablename__ = 'y_train'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    location1 = db.Column(db.Float, nullable=False)
    location2 = db.Column(db.Float, nullable=False)
    location3 = db.Column(db.Float, nullable=False)
    location4 = db.Column(db.Float, nullable=False)
    location5 = db.Column(db.Float, nullable=False)
    location6 = db.Column(db.Float, nullable=False)
    location7 = db.Column(db.Float, nullable=False)
    location8 = db.Column(db.Float, nullable=False)
    location9 = db.Column(db.Float, nullable=False)
    location10 = db.Column(db.Float, nullable=False)
    location11 = db.Column(db.Float, nullable=False)
    location12 = db.Column(db.Float, nullable=False)
    location13 = db.Column(db.Float, nullable=False)
    location14 = db.Column(db.Float, nullable=False)
    location15 = db.Column(db.Float, nullable=False)
    location16 = db.Column(db.Float, nullable=False)
    location17 = db.Column(db.Float, nullable=False)
    location18 = db.Column(db.Float, nullable=False)
    location19 = db.Column(db.Float, nullable=False)
    location20 = db.Column(db.Float, nullable=False)
    location21 = db.Column(db.Float, nullable=False)
    location22 = db.Column(db.Float, nullable=False)
    location23 = db.Column(db.Float, nullable=False)
    location24 = db.Column(db.Float, nullable=False)
    location25 = db.Column(db.Float, nullable=False)
    location26 = db.Column(db.Float, nullable=False)
    location27 = db.Column(db.Float, nullable=False)
    location28 = db.Column(db.Float, nullable=False)
    location29 = db.Column(db.Float, nullable=False)
    location30 = db.Column(db.Float, nullable=False)
    location31 = db.Column(db.Float, nullable=False)
    location32 = db.Column(db.Float, nullable=False)
    location33 = db.Column(db.Float, nullable=False)
    location34 = db.Column(db.Float, nullable=False)
    location35 = db.Column(db.Float, nullable=False)
    location36 = db.Column(db.Float, nullable=False)
    location37 = db.Column(db.Float, nullable=False)


class YTest(db.Model):
    __tablename__ = 'y_test'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    location1 = db.Column(db.Float, nullable=False)
    location2 = db.Column(db.Float, nullable=False)
    location3 = db.Column(db.Float, nullable=False)
    location4 = db.Column(db.Float, nullable=False)
    location5 = db.Column(db.Float, nullable=False)
    location6 = db.Column(db.Float, nullable=False)
    location7 = db.Column(db.Float, nullable=False)
    location8 = db.Column(db.Float, nullable=False)
    location9 = db.Column(db.Float, nullable=False)
    location10 = db.Column(db.Float, nullable=False)
    location11 = db.Column(db.Float, nullable=False)
    location12 = db.Column(db.Float, nullable=False)
    location13 = db.Column(db.Float, nullable=False)
    location14 = db.Column(db.Float, nullable=False)
    location15 = db.Column(db.Float, nullable=False)
    location16 = db.Column(db.Float, nullable=False)
    location17 = db.Column(db.Float, nullable=False)
    location18 = db.Column(db.Float, nullable=False)
    location19 = db.Column(db.Float, nullable=False)
    location20 = db.Column(db.Float, nullable=False)
    location21 = db.Column(db.Float, nullable=False)
    location22 = db.Column(db.Float, nullable=False)
    location23 = db.Column(db.Float, nullable=False)
    location24 = db.Column(db.Float, nullable=False)
    location25 = db.Column(db.Float, nullable=False)
    location26 = db.Column(db.Float, nullable=False)
    location27 = db.Column(db.Float, nullable=False)
    location28 = db.Column(db.Float, nullable=False)
    location29 = db.Column(db.Float, nullable=False)
    location30 = db.Column(db.Float, nullable=False)
    location31 = db.Column(db.Float, nullable=False)
    location32 = db.Column(db.Float, nullable=False)
    location33 = db.Column(db.Float, nullable=False)
    location34 = db.Column(db.Float, nullable=False)
    location35 = db.Column(db.Float, nullable=False)
    location36 = db.Column(db.Float, nullable=False)
    location37 = db.Column(db.Float, nullable=False)

