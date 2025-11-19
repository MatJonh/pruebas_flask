from flask import Blueprint, jsonify, request
from ..extensions import db

users_bp = Blueprint("users_bp", __name__)

@users_bp.route("/", methods=["GET"])
def get_users():
    return jsonify([]), 200

@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    return jsonify(data), 201
