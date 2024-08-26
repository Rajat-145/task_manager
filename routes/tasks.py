from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Task  # Absolute import
from app import db  # Absolute import

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/add', methods=['POST'])
@jwt_required()
def add_task():
    user_id = get_jwt_identity()
    data = request.get_json()

    new_task = Task(
        title=data.get('title'),
        description=data.get('description'),
        status=data.get('status'),
        priority=data.get('priority'),
        due_date=data.get('due_date'),
        user_id=user_id
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task added successfully!"}), 201

@tasks_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    tasks_list = [{"id": task.id, "title": task.title, "description": task.description, "status": task.status,
                   "priority": task.priority, "due_date": task.due_date} for task in tasks]

    return jsonify(tasks_list), 200
