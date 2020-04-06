from flask import jsonify
import os
from services.email.email_service import send_verification_email
from services.token.token_service import generate_token, token_is_valid

from errors.init_error_handler import create_api_error_response
from errors.authorization_errors.authorization_error import UserNotFound, WrongCredentials, UserAlreadyExists, \
    InitValidationError

from models.user import User
import jwt
import bcrypt
from dotenv import load_dotenv
from db.db import db

load_dotenv()

def login_user(email, password):
    try:
        user = User.query.filter_by(email=email).first()
        print(user)
    except Exception:
        raise UserNotFound("email", email)

    if not compare_passwords(password, user.password):
        raise WrongCredentials

    return create_token(user.id, user.is_verified)


def register_user(user):
    if user_exist(user.email):
        raise UserAlreadyExists(user.email)

    try:
        user.password = get_hashed_password(user.password)
        db.session.add(user)
        db.session.commit()
        verification_token = generate_token(user)
        send_verification_email(user.name, user.email, verification_token.token)
    except Exception or ValidationError as e:
        print(str(e))
        raise InitValidationError(str(e))

    return create_token(user.id, user.is_verified)


def verify_user(user_id, token):
    user_to_verify = find_user_by_id(user_id)
    print(user_to_verify.isVerified)
    try:
        token_is_valid(user_id, token)
    except Exception:
        raise Exception

    try:
        user_to_verify.isVerified = True
        user_to_verify.save()
        print(user_to_verify)
    except Exception:
        raise Exception

    return create_token(user_to_verify.id, user_to_verify.isVerified)


def user_exist(email):
    exists = db.session.query(User).filter_by(email=email).scalar() is not None
    if exists:
        return True
    return False


def get_hashed_password(plain_text_password):
    hashed_pwd = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pwd.decode('utf-8')


def compare_passwords(password_from_db, password_to_check):
    return bcrypt.checkpw(password_from_db.encode('utf8'), password_to_check.encode('utf8'))


def create_token(user_id, user_verified):
    try:
        payload = {'id': str(user_id), 'is_verified': user_verified}
        return {'token': jwt.encode(
            payload,
            os.getenv("JWT_KEY"),
            os.getenv("JWT_ALGORITHM")          
        ).decode('UTF-8')}
    except Exception as e:
        raise Exception


def find_user_by_id(user_id):
    try:
        return User.objects.get(id=user_id)
    except Exception:
        raise UserNotFound("id", user_id)


def convert_user_to_json_response(user):
    return jsonify({'id': str(user.id),
                    'name': user.name,
                    'surname': user.surname,
                    'isVerified': user.isVerified
                    })
