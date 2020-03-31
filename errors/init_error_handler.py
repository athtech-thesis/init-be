from flask import jsonify, make_response


def create_api_error_response(status_code, message):
    response = jsonify({
        'status': status_code,
        'message': message
    })
    response.status_code = status_code
    return response


def overwrite_flask_error(message, status_code):
    return make_response(jsonify(message), status_code)



