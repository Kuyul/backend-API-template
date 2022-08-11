from flask.views import MethodView
from flask import request
from chatapp.template import make_output

from chatapp.users.service.service import UserService
from chatapp.users.model.user import UserInfo, GetUserInfoRequest


class UserController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        validate = GetUserInfoRequest.Schema().load(request.get_json(force=True, silent=True))
        user_info = self.service.get_user(validate)

        resp_schema = UserInfo.Schema()

        return make_output(data=resp_schema.dump(user_info), status="ok", error=None)
