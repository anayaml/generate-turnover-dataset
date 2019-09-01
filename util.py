import os
from geopy.geocoders import Yandex

geolocator = Yandex(api_key='bb550fcb-9d8a-4373-8c17-70dec05aa431',lang='en_US',timeout=10)

def verifyInvalidAttr(text):
    return not text

def verifySpamAttr(text):
    return 'lorem ipsum' in str(text).lower()

def getCountry(cityName):
    try:
        location = geolocator.geocode(cityName)
        local = str(location.address)
        listadress = local.split(', ')
        countryIndex = len(listadress)-1
        return listadress[countryIndex]
    except AttributeError:
        return 'Location not found'