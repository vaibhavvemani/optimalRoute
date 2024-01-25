from flask import Flask, Response, request
import requests
import os

app = Flask(__name__)
maps_api_key = os.environ.get('MAPS_API_KEY')

@app.get('/getplaces')
def sendRequest():
    d_placeid = request.args.get("d_place")
    vehicle_type = request.args.get("vtype")
    r = requests.post(
        "https://places.googleapis.com/v1/places:searchNearby", 
        headers={
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': maps_api_key,
            'X-Goog-FieldMask': 'places.displayName'
        },
        json={
            "includedTypes": ["restaurant"],
            "maxResultCount": 10,
            "locationRestriction": {
                "circle": {
                "center": {
                    "latitude": 37.7937,
                    "longitude": -122.3965},
                "radius": 500.0
                }
            }
        }
    )
    response = Response(r.text) 
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response