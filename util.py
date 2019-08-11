import os
from geopy.geocoders import Yandex

geolocator = Yandex(lang='en_US')

def verifyInvalidAttr(text):
    return not text

def verifySpamAttr(text):
    return 'lorem ipsum' in text.lower()

def getCountry(cityName):
    location = geolocator.geocode(cityName)
    local = str(location.address)
    listadress = local.split(', ')
    countryIndex = len(listadress)-1
    return listadress[countryIndex]