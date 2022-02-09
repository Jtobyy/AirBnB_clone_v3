#!/usr/bin/python3
"""
Defines the status route of the app_views blueprint.
status route returns the status of the api
"""

from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def status():
    return {
        "status": "OK"
    }

@app_views.route('/stats')
def stats():
    return {
        "amenities": storage.count("amenities"),
        "cities": storage.count("cities"),
        "places": storage.count("places"),
        "reviews": storage.count("reviews"),
        "states": storage.count("states"),
        "users": storage.count("users")
    }
