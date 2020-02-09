from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def json_response(status_code, message=None):
    payload = {'status_code': HTTP_STATUS_CODES.get(status_code, 'Unknown')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def successful(message):
    return json_response(200, message)


def created(message):
    return json_response(201, message)


def bad_request(message):
    return json_response(400, message)


def unauthorized(message):
    return json_response(401, message)


def forbidden(message):
    return json_response(403, message)


def not_found(message):
    return json_response(404, message)


def conflict(message):
    return json_response(409, message)


def server_error(message):
    return json_response(500, message)