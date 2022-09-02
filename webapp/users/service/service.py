from webapp.users.dao.dao import UserDAO


class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def template(self, user_id: str):
        return self.dao.template(user_id)

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
