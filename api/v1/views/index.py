#!/usr/bin/python3
"""
Defines the status route
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status:
    return jsonify({'status': 'OK'})
