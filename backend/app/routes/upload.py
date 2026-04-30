from flask import Blueprint

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["GET"])
def upload():
    return {"message": "Upload endpoint working"}