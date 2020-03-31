from flask import jsonify, request, Blueprint
from errors.authorization_errors.authorization_error import FormattingError, MissingData, UserAlreadyExists
from errors.init_error_handler import create_api_error_response
from models.user import User
from services.user import user_service
from utils.vaildators.validator import validate_json_request, is_valid_json

api = Blueprint('authorization_controller', __name__, url_prefix='/api/v1.0/auth')


# noinspection PyBroadException
@api.route('/login', methods=['POST'])
def login():

    try:
        is_valid_json(request)
    except BaseException or ValueError or FormattingError:
        return create_api_error_response(FormattingError().status, FormattingError().message)

    json_request = request.get_json()

    try:
        validate_json_request(json_request, 'email', 'password')
    except MissingData as e:
        return create_api_error_response(e.status, e.message)

    email = json_request['email']
    password = json_request['password']
    try:
        return jsonify(user_service.login_user(email, password)), 200
    # Catching all exceptions from server or framework
    except BaseException as e:
        return create_api_error_response(status_code=e.status, message=e.message)


@api.route('/register', methods=['POST'])
def register():


    if not is_valid_json(request):
        return create_api_error_response(FormattingError().status, FormattingError().message)
        
    json_request = request.get_json()

    try:
        validate_json_request(json_request, 'email', 'password', 'name', 'surname')
    except MissingData as e:
        return create_api_error_response(e.status, e.message)

    name = json_request['name']
    surname = json_request['surname']
    email = json_request['email']
    password = json_request['password']

    user_to_register = User(name=name, surname=surname, email=email, password=password)

    try:
        return jsonify(user_service.register_user(user_to_register)), 200
    except UserAlreadyExists as e:
        return create_api_error_response(status_code=500, message=e.message)

@api.route('/verify', methods=['POST'])
def verify():
    
    try:
        print(request)
        is_valid_json(request)
    except InitException or ValueError or FormattingError or TypeError:
        return create_api_error_response(FormattingError().status, FormattingError().message)

    json_request = request.get_json()

    try:
        validate_json_request(json_request, 'user_id', 'token')
    except MissingData as e:
        return create_api_error_response(e.status, e.message)

    user_id = json_request['user_id']
    token = json_request['token']

    try:
        return jsonify(user_service.verify_user(user_id, token))
    except Exception as e:
        return create_api_error_response(status_code=500, message=str(e))


@api.route('/logout', methods=['POST'])
def logout():
    pass
