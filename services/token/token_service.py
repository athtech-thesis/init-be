import datetime
import uuid

from errors.authorization_errors.authorization_error import TokenNotFound, TokenHasExpired, MoreThanOneTokensFound
from models.token import Token
from dotenv import load_dotenv
from db.db import db

load_dotenv()

def generate_token(user):
    token = Token(user_id= user.id, token=generate_verification_token())
    try:
        db.session.add(token)
        db.session.commit()
        return token
    except Exception:
        raise Exception


def generate_verification_token():
    return uuid.uuid4().hex


def token_is_valid(user_id, token):
    try:
        # FIXME
        tokens_from_db = VerificationToken.objects(user=user_id, token=token)
        user_has_one_token(tokens_from_db)
        token_to_check = tokens_from_db[0]
    except Exception:
        raise TokenNotFound

    if token_to_check.expiresAt < datetime.datetime.now():
        raise TokenHasExpired

    return token_to_check


def user_has_one_token(tokens):
    print(len(tokens))
    if len(tokens) > 1:
        raise MoreThanOneTokensFound
    return