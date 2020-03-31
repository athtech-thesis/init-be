from flask import Blueprint, request
# from bson import json_util
from errors.authorization_errors.authorization_error import MissingData, UserNotFound
from errors.init_error_handler import create_api_error_response
from services.user import user_service

api = Blueprint('user_controller', __name__, url_prefix='/api/v1.0/user')


@api.route('/<user_id>', methods=['GET'])
def get_user(user_id):

    try:
        user_id = user_id
        print(user_id)
    except Exception:
        return create_api_error_response(MissingData().status, MissingData().message)

    try:
        user_to_retrieve = user_service.find_user_by_id(user_id)
    except UserNotFound as e:
        return create_api_error_response(e.status, e.message)

    return user_service.convert_user_to_json_response(user_to_retrieve)


@api.route('/user')
def rr():
    return 'hello'
