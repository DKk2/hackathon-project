"""Flask entrypoint for Smart Campus Navigation System."""

from __future__ import annotations

from flask import Flask, send_from_directory
from flask_cors import CORS

from models import init_db
from routes import api


def create_app() -> Flask:
    app = Flask(__name__, static_folder="../frontend", static_url_path="")
    CORS(app)

    init_db()
    app.register_blueprint(api)

    @app.get("/")
    def serve_frontend():
        return send_from_directory("../frontend", "index.html")

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000, debug=True)
