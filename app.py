#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, abort, request
from flask.ext.sqlalchemy import SQLAlchemy

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
    return render_template('site_map.html', dict=dict)


@app.route('/car/')
@app.route('/car/<int:car_id>')
def car(car_id=None):
    if car_id:
        car = Car.query.get(car_id)
        ratings = Rating.query.filter_by(car_id=car_id).all()
        return render_template('car.html', car=car, ratings=ratings)

    cars = Car.query.all()
    return render_template('templates/cars.html', cars=cars)

@app.route('/rate', methods=['POST'])
def rate():
    print(request.json)
    print(request.data)
    if not request.json:
        abort(400)

    rating = Rating(
        name = request.json['name'],
        rating = request.json['rating'],
        car_id = request.json['car_id']
    )

    db.session.add(rating)
    db.session.commit()

    return jsonify(rating), 201


if __name__ == '__main__':
    app.debug = True
    app.run()
