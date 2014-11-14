# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % os.path.dirname(os.path.abspath(__file__))
db = SQLAlchemy(app)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('templates/index.html', dict=dict)

@app.route('/about')
def about():
    return render_template('templates/about.html', dict=dict)

@app.route('/car/')
@app.route('/car/<int:car_id>')
def car(car_id=None):
    return "derp %d" % car_id
    return render_template('templates/car.html', dict=dict)
    return render_template('templates/cars.html', dict=dict)



if __name__ == '__main__':
    app.debug = True
    app.run()
