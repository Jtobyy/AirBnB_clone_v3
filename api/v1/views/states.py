#!/usr/bin/python3
"""
Handles all default RESTFUL API actions
"""

from api.v1.views import app_views
from flask import make_response, jsonify, abort, request
from models import storage


@app_views.route('/states', methods=['GET'])
def get_states():
    states = storage.all("State")
    states_list = []
    i = 0
    for val in states:
        states_list[i] = val.to_dict()
        i += 1
    return make_response(jsonify(states_list))


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state_by_id(state_id):
    obj = storage.get("State", state_id)
    if obj is not None:
        return obj.to_dict()
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state_by_id(state_id):
    obj = storage.get("State", state_id)
    if obj is not None:
        storage.delete(obj)
        return make_response(jsonify({}), 200)
    else:
        abort(404)


@app_views.route('/states/', methods=['POST'])
def send_state():
    request_data = request.get_json()
    try:
        json.loads(request_data)
    except ValueError:
        make_response("Not a JSON", 400)
    state = request_data['name']
    if state is None:
        make_response("Missing name", 400)
    else:
        obj = storage.new(state)
        storage.save()
        return make_response(state.to_dict(), 201)


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state_by_id(state_id):
    obj = storage.get("State", state_id)
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
