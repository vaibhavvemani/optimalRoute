from flask import Flask
import requests
import os

app = Flask(__name__)
maps_api_key = os.environ.get('MAPS_API_KEY')

@app.get('/getroute')
def sendRequest():
    response = requests.post(
        "https://routes.googleapis.com/directions/v2:computeRoutes", 
        headers={
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': maps_api_key,
            'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline',
        },
        data={
            "origin":{
                "placeId": "ChIJayOTViHY5okRRoq2kGnGg8o"
            },
            "destination":{
                "placeId": "ChIJTYKK2G3X5okRgP7BZvPQ2FU"
            },
            "travelMode": "DRIVE",
            "routingPreference": "TRAFFIC_AWARE",
            "departureTime": "2024-10-15T15:01:23.045123456Z",
            "computeAlternativeRoutes": False,
            "routeModifiers": {
                "avoidTolls": False,
                "avoidHighways": False,
                "avoidFerries": False
            },
            "languageCode": "en-US",
            "units": "IMPERIAL"
        }
    )
    return response.text


