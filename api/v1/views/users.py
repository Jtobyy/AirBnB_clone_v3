#!/usr/bin/python3
"""
Handles all default RESTFUL API actions
"""

from api.v1.views import app_views
from flask import make_response, jsonify, abort, request
from models import storage


@app_views.route('/users', methods=['GET'])
def get_users():
    users = storage.all("User")
    users = storage.all("City")
    users_list = []
    i = 0
    for val in users:
        users_list[i] = val.to_dict()
        i += 1
    return make_response(jsonify(users_list))


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    obj = storage.get("User", user_id)
    if obj is not None:
        return obj.to_dict()
    else:
        abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    obj = storage.get("User", user_id)
    if obj is not None:
        storage.delete(obj)
        return make_response(jsonify({}), 200)
    else:
        abort(404)


@app_views.route('/users/', methods=['POST'])
def send_user():
    request_data = request.get_json()
    try:
        json.loads(request_data)
    except ValueError:
        make_response("Not a JSON", 400)
    user = request_data['name']
    if user is None:
        make_response("Missing name", 400)
    else:
        obj = storage.new(user)
        storage.save()
        return make_response(user.to_dict(), 201)


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    obj = storage.get("User", user_id)
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
