from flask import Blueprint, request, jsonify
from app.services.parser import parse_csv

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400
    
    try:
        transactions = parse_csv(file)
        return jsonify({"transactions": transactions}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500