from flask import Blueprint, jsonify, render_template
bp = Blueprint('main', __name__)

@bp.before_app_request
def debug_log():
    print("A request is being processed...")

@bp.after_app_request
def after_debug_log(response):
    print("A request has been processed.")

@bp.route("hello", methods=["GET"])
def hello():
    print("Processing hello request...")
    results = {
        "message": "Hello, World!",
        "status": "success"
    }
    return jsonify(results), 200

@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html"), 200