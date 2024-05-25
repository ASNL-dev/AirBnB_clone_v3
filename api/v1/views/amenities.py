#!/usr/bin/python3
"""ameneties.py"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.amenity import Amenity

@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """Get amenity information for all amenities"""
    amenities = [amenity.to_dict() for amenity in storage.all("Amenity").values()]
    return jsonify(amenities)

@app_views.route('/amenities/<string:amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Get amenity information for specified amenity"""
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())

@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Delete an amenity based on its amenity_id"""
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """Create a new amenity"""
    req_data = request.get_json()
    if not req_data:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in req_data:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    amenity = Amenity(**req_data)
    amenity.save()
    return make_response(jsonify(amenity.to_dict()), 201)

@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """Update an amenity"""
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in req_data.items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, attr, val)
    amenity.save()
    return jsonify(amenity.to_dict())
