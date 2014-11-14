# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template

from models import *

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/about')
def about():
    return render_template('templates/about.html')

@app.route('/faq')
def faq():
    return render_template('templates/faq.html')

@app.route('/contact')
def contact():
    return render_template('templates/contact.html')

@app.route('/sitemap')
def sitemap():
    return render_template('templates/site_map.html', dict=dict)


@app.route('/car/')
@app.route('/car/<int:car_id>')
def car(car_id=None):
    if car_id:
        car = Car.query.get(car_id)
        return render_template('templates/car.html', car=car)

    cars = Car.query.all()
    return render_template('templates/cars.html', cars=cars)



if __name__ == '__main__':
    app.debug = True
    app.run()
