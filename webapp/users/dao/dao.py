from common_lib.infra.mysql import DB


class UserDAO:
    def __init__(self):
        self.db = DB()

    def template(self, user_id):
        query = """
                SELECT id 
                , first_name
                , last_name
                , prof_pic_url
                , email
                FROM user
                WHERE USER_ID = %(user_id)s
                """
                
        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "user_id": user_id
            })
            row = cursor.fetchone()
            
            user = {
                "user_id": row['USER_ID'],
                "email": row['EMAIL'],
                "first_name": row['FIRST_NAME'],
                "last_name": row['LAST_NAME'],
                "prof_pic_url": row['PROF_PIC_URL']
            }

            return user
