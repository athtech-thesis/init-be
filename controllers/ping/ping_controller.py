from flask import jsonify, request, Blueprint

api = Blueprint('ping_controller', __name__, url_prefix='/api/v1.0/ping')

@api.route('/', methods=['GET'])
def ping():
    return "PONG"
