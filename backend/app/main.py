from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.upload import upload_bp
    app.register_blueprint(upload_bp)

    return app