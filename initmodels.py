# -*- coding: utf-8 -*-

from models import *
from app import db

descriptions = {
    "v40": "The Volvo V40 is a small family car, available in five-door hatchback form, that was unveiled at the 2012 Geneva Motor Show. It has been on sale in Europe since May 2012 and the UK since August.",

    "up": "The Volkswagen up! is a city car, part of the Volkswagen Group New Small Family (NSF) series of models, unveiled at the 2011 Frankfurt Motor Show (IAA). Production of the up! started in December 2011 at the Volkswagen Bratislava Plant in Bratislava, Slovakia.",

    "ds3": "The Citroën DS3 is a supermini, produced by the French manufacturer Citroën since 2009 and officially launched in January 2010. This is the first car in the new DS (pronounced déesse, which is French for goddess) range from Citroën. It was first hinted by the concept car Citroën DS Inside. While DS branding explicitly recalls the classic Citroën DS, the DS3 bears no resemblance to the older car and shares none of its engineering quirks.",

    "500": "The 500 is available with four different trim levels: Naked (not available in the United Kingdom or Italy; opting for this trim level means that the car does not have the seven airbags meaning that the passenger safety rating drops), Pop, Lounge, and Sport. Customers can also choose between 15 interior trims, nine wheel options, 19 decals, and 12 body colours. There are over 500,000 different personalized combinations of the 500 that can be made by adding all kinds of accessories, decals, interior and exterior colours, and trims. The car is also available with the Blue&Me navigation system. The American Sport version has the 1.4 litre Multiair engine, which is manufactured in Michigan.",

    "polo": "The Volkswagen Polo is a supermini car produced by the German manufacturer Volkswagen since 1975. It is sold in Europe and other markets worldwide in hatchback, sedan, coupé and estate variants.",

    "yaris": "The Toyota Yaris is a subcompact car produced by Toyota since 1999, replacing the Starlet. Between 1999 and 2005, some markets received the same vehicles under the Toyota Echo name. Toyota has used the Yaris and Echo names on the export version of several different Japanese-market models.",

    "c180": "The Mercedes-Benz C-Class is a line of compact executive cars produced by Daimler AG. Introduced in 1993 as a replacement for the 190 (W201) range, the C-Class was the smallest model in the marques lineup until the A-Class arrived in 1997.",

}

images = {
    "v40": '/static/img/volvo_v40.png',
    "up": '/static/img/vw_up.png',
    "ds3": '/static/img/citroen_ds3.png',
    "500": '/static/img/fiat_500.png',
    "polo": '/static/img/vw_polo_auto.png',
    "yaris": '/static/img/toyota_yaris_auto.png',
    "c180": '/static/img/mercedes_c180.png',
}

db.create_all()

car_one = Car('Volvo', 'V40', 299.0, description=descriptions["v40"], picture_url=images['v40'])
car_two = Car('Volkswagen', 'Up', 199.0, description=descriptions["up"], picture_url=images['up'])
car_three = Car('Citroen', 'DS3', 249.0, description=descriptions["ds3"], picture_url=images['ds3'])
car_four = Car('Fiat', '500', 189.0, description=descriptions["500"], picture_url=images['500'])
car_five = Car('Volkswagen', 'Polo Auto', 179.0, description=descriptions["polo"], picture_url=images['polo'], available=False)
car_six = Car('Toyota', 'Yaris Auto', 189.0, description=descriptions["yaris"], picture_url=images['yaris'])
car_seven = Car('Mercedes', 'C180', 389.0, description=descriptions["c180"], picture_url=images['c180'])

db.session.add(car_one)
db.session.add(car_two)
db.session.add(car_three)
db.session.add(car_four)
db.session.add(car_five)
db.session.add(car_six)
db.session.add(car_seven)

db.session.commit()

