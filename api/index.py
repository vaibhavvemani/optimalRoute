from flask import Flask, Response, request
import requests
import os

app = Flask(__name__)
maps_api_key = os.environ.get('MAPS_API_KEY')

@app.get('/getroute')
def sendRequest():
    o_placeid = request.args.get("o_place")
    d_placeid = request.args.get("d_place")
    vehicle_type = request.args.get("vtype")
    r = requests.post(
        "https://routes.googleapis.com/directions/v2:computeRoutes", 
        headers={
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': maps_api_key,
            'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline,routes.travelAdvisory,routes.legs.travelAdvisory'
        },
        json={
            "origin":{
                "placeId": f"{o_placeid}"
            },
            "destination":{
                "placeId": f"{d_placeid}"
            },
            "routeModifiers": {
                "vehicleInfo": {
                    "emissionType": f"{vehicle_type}"
                },
                "avoidTolls": False,
                "avoidHighways": False,
                "avoidFerries": False
            },
            "travelMode": "DRIVE",
            "routingPreference": "TRAFFIC_AWARE_OPTIMAL",
            "extraComputations": ["TRAFFIC_ON_POLYLINE"],
            "departureTime": "2024-10-15T15:01:23.045123456Z",
            "computeAlternativeRoutes": False,
            "languageCode": "en-US",
            "units": "IMPERIAL"
        }
    )
    response = Response(r.text) 
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.get('/getusroute')
def getRoute():
    o_placeid = request.args.get("o_place")
    d_placeid = request.args.get("d_place")
    r = requests.post(
        "https://routes.googleapis.com/directions/v2:computeRoutes", 
        headers={
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': maps_api_key,
            'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline,routes.routeLabels,routes.routeToken,routes.travelAdvisory,routes.legs.travelAdvisory'
        },
        json={
            "origin":{
                "placeId": f"{o_placeid}"
            },
            "destination":{
                "placeId": f"{d_placeid}"
            },
            "routeModifiers": {
                "vehicleInfo": {
                    "emissionType": "GASOLINE"
                },
                "avoidTolls": False,
                "avoidHighways": False,
                "avoidFerries": False
            },
            "travelMode": "DRIVE",
            "routingPreference": "TRAFFIC_AWARE_OPTIMAL",
            "extraComputations": ["TRAFFIC_ON_POLYLINE"],
            "requestedReferenceRoutes": ["FUEL_EFFICIENT"],
            "departureTime": "2024-10-15T15:01:23.045123456Z",
            "computeAlternativeRoutes": False,
            "languageCode": "en-US",
            "units": "IMPERIAL"
        }
    )
    response = Response(r.text) 
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
