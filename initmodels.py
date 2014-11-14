# -*- coding: utf-8 -*-

from models import *
from app import db

descriptions = {
    "v40": "The Volvo V40 is a small family car, available in five-door hatchback form, that was unveiled at the 2012 Geneva Motor Show. It has been on sale in Europe since May 2012 and the UK since August.",

    "up": "The Volkswagen up! is a city car, part of the Volkswagen Group New Small Family (NSF) series of models, unveiled at the 2011 Frankfurt Motor Show (IAA). Production of the up! started in December 2011 at the Volkswagen Bratislava Plant in Bratislava, Slovakia.",

    "ds3": "The Citroën DS3 is a supermini, produced by the French manufacturer Citroën since 2009 and officially launched in January 2010. This is the first car in the new DS (pronounced déesse, which is French for goddess) range from Citroën. It was first hinted by the concept car Citroën DS Inside. While DS branding explicitly recalls the classic Citroën DS, the DS3 bears no resemblance to the older car and shares none of its engineering quirks.",

    "500": "The Fiat 500 (Italian: Cinquecento, Italian pronunciation: [ˌtʃiŋkweˈtʃɛnto]) is a city car produced by the Italian manufacturer Fiat between 1957 and 1975.",

    "polo": "The Volkswagen Polo (pronounced [ˈfɔlksˌvaːgən ˈpoːloː]) is a supermini car produced by the German manufacturer Volkswagen since 1975. It is sold in Europe and other markets worldwide in hatchback, sedan, coupé and estate variants.",

    "yaris": "The Toyota Yaris is a subcompact car produced by Toyota since 1999, replacing the Starlet. Between 1999 and 2005, some markets received the same vehicles under the Toyota Echo name. Toyota has used the Yaris and Echo names on the export version of several different Japanese-market models.",

    "c180": "The Mercedes-Benz C-Class is a line of compact executive cars produced by Daimler AG. Introduced in 1993 as a replacement for the 190 (W201) range, the C-Class was the smallest model in the marques lineup until the A-Class arrived in 1997.",

    "s": "The Tesla Model S is a full-sized electric five-door, luxury liftback, produced by Tesla Motors. Since its introduction in June 2012 it has achieved rapidly growing sales, particularly in Norway and California. It scored a perfect 5.0 NHTSA safety rating. The US Environmental Protection Agency (EPA) official range for the Model S Performance model equipped with an 85 kWh battery pack is 265 miles (426 km), topping the Tesla Roadster to lead the electric car market. EPA rates its energy consumption at 237.5 Wh per kilometer (38 kWh/100 mi) for a combined fuel economy of 89 miles per gallon gasoline equivalent (2.64 L/100 km).",

    "m7": "BMW permitted Alpina to produce a high-performance version of its flagship 7-Series, however they did not want it to be a high-revving, BMW M version (which would have been known as a BMW M7 under the current nomenclature). It has also been suggested that there was no market for an M7 that would have featured the BMW M's trademark high-rev engine and twin-clutch automated manual transmission, and most customers who desired a performance option in the 7 Series would have gone for the V12-engined BMW 760Li.",
}

db.create_all()

car_one = Car('Volvo', 'V40', 299.0, description=descriptions["v40"])
car_two = Car('Volkswagen', 'Up', 199.0, description=descriptions["up"])
car_three = Car('Citroen', 'DS3', 249.0, description=descriptions["ds3"])
car_four = Car('Fiat', '500', 189.0, description=descriptions["500"])
car_five = Car('Volkswagen', 'Polo Auto', 179.0, description=descriptions["polo"])
car_six = Car('Toyota', 'Yaris Auto', 189.0, description=descriptions["yaris"])
car_seven = Car('Mercedes', 'C180', 389.0, description=descriptions["c180"])
car_eight = Car('Tesla', 'S', 459.0, description=descriptions["s"])
car_nine = Car('BMW', 'M7 Touring', 399.0, description=descriptions["m7"])

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

