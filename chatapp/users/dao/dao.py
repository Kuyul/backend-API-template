from typing import Optional

from common_lib.infra.mysql import DB
from chatapp.users.model.user import UserInfo


class UserDAO:
    def __init__(self):
        self.db = DB()

    def get_user(self, user_id) -> Optional[UserInfo]:
        query = """
                SELECT USER_ID 
                , FIRST_NAME
                , LAST_NAME
                , PROF_PIC_URL
                , EMAIL
                FROM CHAT_USER
                WHERE USER_ID = %(user_id)s
                """
        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "user_id": user_id
            })
            row = cursor.fetchone()
            user = UserInfo(
                user_id=row['USER_ID'],
                email=row['EMAIL'],
                first_name=row['FIRST_NAME'],
                last_name=row['LAST_NAME'],
                prof_pic_url=row['PROF_PIC_URL']
            )

            return user
