#!/usr/bin/python3
"""
Defines the status route of the app_views blueprint.
status route returns the status of the api
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status:
    return jsonify({'status': 'OK'})
