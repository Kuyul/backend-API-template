from webapp.users.dao.dao import UserDAO


class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def template(self, user_id: str):
        return self.dao.template(user_id)
