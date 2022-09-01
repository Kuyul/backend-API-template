from flask import Blueprint
from flask_restful import Api
from webapp.users.controller.controller import TemplateController, UserSignUpController

user_blueprint = Blueprint('user', __name__, url_prefix='/api/user')
user_api = Api(user_blueprint)

user_api.add_resource(TemplateController, "/template")
user_api.add_resource(UserSignUpController, "/signup")
