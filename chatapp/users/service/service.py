from chatapp.users.dao.dao import UserDAO
from chatapp.users.model.user import GetUserInfoRequest


class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def get_user(self, req: GetUserInfoRequest):
        return self.dao.get_user(req.user_id)
