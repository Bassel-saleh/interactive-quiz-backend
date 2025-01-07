from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, Question, QuizResult

bp = Blueprint("routes", __name__)

# User registration
@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# User login
@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)
    return jsonify({"token": token}), 200

# Get questions
@bp.route("/questions", methods=["GET"])
def get_questions():
    questions = Question.query.all()
    output = [{"id": q.id, "question": q.question, "options": q.options} for q in questions]
    return jsonify(output), 200

# Submit quiz
@bp.route("/quiz/submit", methods=["POST"])
@jwt_required()
def submit_quiz():
    user_id = get_jwt_identity()
    data = request.get_json()
    answers = data.get("answers")
    
    score = 0
    for answer in answers:
        question = Question.query.get(answer["id"])
        if question and question.correct_answer == answer["answer"]:
            score += 1

    result = QuizResult(user_id=user_id, score=score)
    db.session.add(result)
    db.session.commit()
    return jsonify({"score": score}), 200

# Get user results
@bp.route("/results", methods=["GET"])
@jwt_required()
def get_results():
    user_id = get_jwt_identity()
    results = QuizResult.query.filter_by(user_id=user_id).all()
    output = [{"score": r.score, "timestamp": r.timestamp} for r in results]
    return jsonify(output), 200
