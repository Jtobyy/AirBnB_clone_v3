#!/usr/bin/python3
"""
Defines the status route of the app_views blueprint.
status route returns the status of the api
"""

from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    '''returns status of the api'''
    return jsonify(
        status="OK"
        )


@app_views.route('/stats', methods=['GET'])
def stats():
    '''returns stats of models'''
    return jsonify(
        amenities=storage.count("amenities"),
        cities=storage.count("cities"),
        places=storage.count("places"),
        reviews=storage.count("reviews"),
        states=storage.count("states"),
        users=storage.count("users")
    )
