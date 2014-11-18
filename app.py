#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, abort, request, jsonify, Response
from flask.ext.sqlalchemy import SQLAlchemy

from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as ET



from models import *

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sitemap')
def sitemap():
    cars=Car.query.all()
    return render_template('site_map.html', cars=cars)

@app.route('/tos')
def tos():
    return render_template('tos.html')


@app.route('/car/')
@app.route('/car/<int:car_id>')
def car(car_id=None):

    cars = Car.query.all()

    if car_id:
        car = Car.query.get(car_id)
        if car_id == len(cars):
            next_car = 1
        else:
            next_car = car_id + 1

        if car_id == 1:
            prev_car = len(cars)
        else:
            prev_car = car_id - 1

        ratings = Rating.query.filter_by(car_id=car_id).all()
        num_ratings = len(ratings)

        return render_template('car.html', car=car, ratings=ratings, num_ratings=num_ratings, prev_car=prev_car, next_car=next_car)

    return render_template('cars.html', cars=cars)

@app.route('/rate', methods=['POST'])
def rate():
    print(request.json)
    print(request.data)
    if not request.json:
        abort(400)

    rating = Rating(
        request.json['name'],
        request.json['car_id'],
        request.json['rating']
    )

    db.session.add(rating)
    db.session.commit()

    ratings = Rating.query.filter_by(car_id = request.json['car_id']).all()
    return jsonify(reviews = [rating.serialize for rating in ratings]), 201

@app.route('/car/xml/')
def car_xml():
    cars = Car.query.all()

    xml = Element('cars')

    for car in cars:
        carElement = SubElement(xml, 'car')

        id = SubElement(carElement, 'id')
        id.text = str(car.id)

        brand = SubElement(carElement, 'brand')
        brand.text = car.brand

        model = SubElement(carElement, 'model')
        model.text = car.model

        price = SubElement(carElement, 'price')
        price.text = str(car.price)

        description = SubElement(carElement, 'description')
        description.text = car.description

        available = SubElement(carElement, 'available')
        available.text = str(car.available)

        picture_url = SubElement(carElement, 'picture_url')
        picture_url.text = car.picture_url

        ratings = Rating.query.filter_by(car_id=car.id).all()
        ratingsElement = SubElement(carElement, 'ratings')

        for rating in ratings:
            ratingElement = SubElement(ratingsElement, 'rating')

            id = SubElement(ratingElement, 'id')
            id.text = str(rating.id)

            name = SubElement(ratingElement, 'name')
            name.text = rating.name

            rate = SubElement(ratingElement, 'rate')
            rate.text = str(rating.rating)


    return Response(tostring(xml), mimetype='text/xml')




if __name__ == '__main__':
    app.debug = True
    app.run()
