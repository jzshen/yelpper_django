from urllib2 import urlopen
import datetime
import time

import json


#def geoCoder(lat, lon)


def getAddress(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    
    components = j['results'][0]['address_components']
    componentsPretty = json.dumps(components)
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "locality" in c['types']:
            town = c['long_name']
        if "administrative_area_level_1" in c["types"]:
            state = c['short_name']
        if "street_number" in c['types']:
            street_number = c['long_name']
        if "route" in c['types']:
            route = c['long_name']
            streetAddress = street_number + " " + route
    address = [streetAddress, town, state]
    return address


#def getCity

lunch = datetime.datetime(2015, 10, 22, 15, 0, 0, 0)

def getMealTime():
    currentTime = datetime.datetime.now()
    currentYear = curretTime.year
    currentMonth = currentTime.month
    currentDay = currentTime.day
    if currentTime < lunch:
        return "lunch"
    else:
        return "dinner"
    

#getAddress(37.8755449, -122.25893279999998)