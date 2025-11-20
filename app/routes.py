from flask import Blueprint, jsonify
from .models import User

users_bp = Blueprint("users", __name__, url_prefix="/api")

@users_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    data = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(data)
