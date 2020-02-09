from flask import request, g

from app import db, bcrypt
from app.models import User, BlacklistToken
from app.api import bp
from app.api.decorators import login_required
from app.api.response import bad_request, server_error, not_found, conflict, unauthorized, forbidden, successful, created


@bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json() or {}

    if 'email' not in data or 'first_name' not in data or 'last_name' not in data or 'password' not in data:
        return bad_request('Must include email, first_name, last_name and password fields')
    if User.query.filter_by(email=data['email']).first():
        return conflict('Please use a different email address')

    try:
        user = User(
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            password=data.get('password')
        )
        db.session.add(user)
        db.session.commit()

        auth_token = user.encode_auth_token(user.id)
        return created(auth_token.decode())
    except Exception as err:
        return server_error(err)


@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json() or {}

    if 'email' not in data or 'password' not in data:
        return bad_request('Must include email and password fields')

    try:
        # fetch the user data
        user = User.query.filter_by(email=data.get('email')).first()
        if user and user.check_password(data.get('password')):
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                return successful(auth_token.decode())
        else:
            return unauthorized('Bad credentials')
    except Exception as err:
        return server_error(err)


@bp.route('/logout', methods=['POST'])
def logout_user():
    auth_token = g.current_auth_token
    blacklist_token = BlacklistToken(token=auth_token)
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        return successful('Successfully logged out.')
    except Exception as err:
        return server_error(err)


@bp.route('/user', methods=['GET'])
@login_required
def retrieve_user():
        user = g.user
        return successful(user.to_dict())