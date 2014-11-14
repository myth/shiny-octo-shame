from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(1000))
    available = db.Column(db.Boolean, default=True)
    picture_url = db.Column(db.String(250))
    ratings = db.relationship('Rating', backref='car', lazy='dynamic')

    def __init__(self, brand, model, price, description=None, picture_url='/static/img/default.jpg', available=True):
        self.brand = brand
        self.model = model
        self.price = price
        self.description = description
        self.available = available
        self.picture_url = picture_url


    def __repr__(self):
        return '<Car %s - %s>' % (self.brand, self.model)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))

    def __init__(self, name, car, rating):
        self.name = name
        self.car_id = car
        self.rating = rating

    def __repr__(self):
        return '<Rating %s: %d>' % (self.name, self.rating)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'car_id': self.car_id,
            'rating': self.rating
        }
