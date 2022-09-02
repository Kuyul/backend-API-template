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
        }
