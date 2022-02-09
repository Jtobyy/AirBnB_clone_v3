#!/usr/bin/python3
"""
Handles all default RESTFUL API actions
"""

from api.v1.views import app_views
from flask import make_response, jsonify, abort, request
from models import storage


@app_views.route('/reviews', methods=['GET'])
def get_reviews():
    storage.all("Review")


@app_views.route('/reviews/<review_id>', methods=['GET'])
def get_review_by_id(review_id):
    obj = storage.get("Review", review_id)
    if obj is not None:
        return obj.to_dict()
    else:
        abort(404)


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review_by_id(review_id):
    obj = storage.get("Review", review_id)
    if obj is not None:
        storage.delete(obj)
        return make_response(jsonify({}), 200)
    else:
        abort(404)


@app_views.route('/reviews/', methods=['POST'])
def send_review():
    request_data = request.get_json()
    try:
        json.loads(request_data)
    except ValueError:
        make_response("Not a JSON", 400)
    review = request_data['name']
    if review is None:
        make_response("Missing name", 400)
    else:
        obj = storage.new(review)
        storage.save()
        return make_response(review.to_dict(), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'])
def update_review_by_id(review_id):
    obj = storage.get("Review", review_id)
    try:
        json.loads(request_data)
    except ValueError:
        make_response("Not a JSON", 400)

    if obj is not None:
        request_data = request.get_json()
        id = obj.id
        created_at = obj.created_at
        updated_at = obj.updated_at
        obj.__dict__.update(request_data)
        obj.__dict__.update({'id': id,
                             'created_at': created_at,
                             'updated_at': updated_at})
        return make_response(obj.to_dict(), 200)
    else:
        abort(404)
