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

    def check_email(self, email: str):
        query = """
        SELECT id from user
        WHERE email = %(email)s
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "email": email
            })
            row = cursor.fetchone()

            if row is not None:
                return True
            else:
                return False

    def signup(self, first_name: str, last_name: str, email: str, username: str, password: str):
        query = """
        INSERT INTO user
        (id, first_name, last_name, email, username, password)
        VALUES
        (%(id)s, %(first_name)s, %(last_name)s, %(email)s, %(username)s, %(password)s);
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "id": str(uuid4()),
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "username": username,
                "password": password
            })
