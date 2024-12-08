from flask import Blueprint, request, jsonify, current_app
from app.models import MemberModel

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/', methods=['GET'])
def get_members():
    member_model = MemberModel(current_app.db)
    members = member_model.get_all()
    return jsonify(members), 200

@members_blueprint.route('/<string:id>', methods=['GET'])
def get_member(id):
    member_model = MemberModel(current_app.db)
    member = member_model.get_by_id(id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

@members_blueprint.route('/', methods=['POST'])
def create_member():
    member_model = MemberModel(current_app.db)
    data = request.json
    member_id = member_model.create(data)
    return jsonify({"message": "Member created", "id": member_id}), 201

@members_blueprint.route('/<string:id>', methods=['PUT'])
def update_member(id):
    member_model = MemberModel(current_app.db)
    data = request.json
    member_model.update(id, data)
    return jsonify({"message": "Member updated"}), 200

@members_blueprint.route('/<string:id>', methods=['DELETE'])
def delete_member(id):
    member_model = MemberModel(current_app.db)
    member_model.delete(id)
    return jsonify({"message": "Member deleted"}), 200
