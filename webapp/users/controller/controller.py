from flask.views import MethodView
from flask import request
from webapp.users.service.service import UserService


class TemplateController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        input_data = request.get_json()
        user_id = input_data['user_id']

        user_info = self.service.template(user_id)

        return {
                "data": user_info,
                "status": "success",
                "message": ""


class UserSignUpController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        input_data = request.get_json()
        first_name = input_data['first_name']
        last_name = input_data['last_name']
        email = input_data['email']
        username = input_data['username']
        password = input_data['password']
        confirm_password = input_data['confirm_password']

        error = self.service.signup(first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    username=username,
                                    password=password,
                                    confirm_password=confirm_password)

        if error is not None:
            return {
                "data": {},
                "status": "fail",
                "message": error
            }
        else:
            return {
                "data": {},
                "status": "success",
                "message": "New user was successfully created"
            }
