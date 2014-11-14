# -*- coding: utf-8 -*-

from models import *
from app import db

db.create_all()

car_one = Car('Volvo', 'V40', 299.0)
car_two = Car('Volkswagen', 'Up', 199.0)
car_three = Car('Citroen', 'DS3', 249.0)
car_four = Car('Fiat', '500', 189.0)
car_five = Car('Volkswagen', 'Polo Auto', 179.0)
car_six = Car('Toyota', 'Yaris Auto', 189.0)
car_seven = Car('Mercedes', 'C180', 389.0)
car_eight = Car('Tesla', 'S', 459.0)
car_nine = Car('BMW', 'M7 Touring', 399.0)

db.session.add(car_one)
db.session.add(car_two)
db.session.add(car_three)
db.session.add(car_four)
db.session.add(car_five)
db.session.add(car_six)
db.session.add(car_seven)
db.session.add(car_eight)
db.session.add(car_nine)

db.session.commit()

