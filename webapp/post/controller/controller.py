from flask.views import MethodView
from flask import request
from webapp.users.service.service import UserService
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
