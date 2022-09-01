from webapp.users.dao.dao import UserDAO
from webapp.users.model.user import GetUserInfoRequest


class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def template(self, req: GetUserInfoRequest):
        return self.dao.template(req.user_id)

    def signup(self,
               first_name: str,
               last_name: str,
               email: str,
               username: str,
               password: str,
               confirm_password: str):

        if confirm_password != password:
            return "Passwords do not match"

        email_exists = self.dao.check_email(email)
        if email_exists:
            return "An account with the same email address exists"

        self.dao.signup(first_name, last_name, email, username, password)
