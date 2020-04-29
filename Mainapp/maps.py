import google maps
import pprint
import time

from GoogleMapsAPIKey import get_my_key

API_KEY = get_my_key()

 gmaps = googlemaps.Client(key=API_KEY)

 places_result = gmaps.places_nearby (location='-33.8670522,151.1957362', radius=40000, open_now=False, type = 'cafe')

 pprint.pprint(places_result)
