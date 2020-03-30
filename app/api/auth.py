from flask import request, g
from marshmallow import Schema, fields, post_load, ValidationError

from app import db, bcrypt
from app.models import User, BlacklistToken
from app.api import bp
from app.api.decorators import login_required
from app.api.response import bad_request, server_error, not_found, conflict, unauthorized, forbidden, successful, created


class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    registered_on = fields.DateTime(dump_only=True)
    password = fields.String(required=True, load_only=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


class LoginSchema(Schema):
    name = fields.Str(required=True)
    password = fields.String(required=True)


@bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json() or {}

    try:
        new_user = UserSchema().load(data)
    except ValidationError as err:
        return bad_request(err.messages)

    try:
        db.session.add(new_user)
        db.session.commit()

        auth_token = new_user.encode_auth_token(new_user.id)
        return created(auth_token.decode())
    except Exception as err:
        return server_error(str(err))


@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json() or {}

    errors = LoginSchema().validate(data)
    if errors:
        return bad_request(errors)

    try:
        # fetch the user data
        user = User.query.filter_by(name=data['name']).first()
        if user and user.check_password(data['password']):
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                return successful(auth_token.decode())
        else:
            return unauthorized('Bad credentials')
    except Exception as err:
        return server_error(str(err))


@bp.route('/logout', methods=['POST'])
def logout_user():
    auth_token = g.current_auth_token
    blacklist_token = BlacklistToken(token=auth_token)
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        return successful('Successfully logged out.')
    except Exception as err:
        return server_error(str(err))


@bp.route('/user', methods=['GET'])
@login_required
def retrieve_user():
        return successful(UserSchema().dump(g.user))