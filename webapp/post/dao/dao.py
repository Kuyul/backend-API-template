from common_lib.infra.mysql import DB
from uuid import uuid4


class PostDAO:
    def __init__(self):
        self.db = DB()

    def share_post(self, user_id, message):
        query = """
        INSERT INTO post
        (id, user_id, message)
        VALUES
        (%(post_id)s, %(user_id)s, %(message)s);
        """

        post_id = str(uuid4())

        params = {
            "post_id": post_id,
            "user_id": user_id,
            "message": message
        }

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, params)

            return post_id

    def get_newsfeed(self, page: int, limit: int):
        offset = (page - 1) * limit

        query = """
        SELECT P.id			    as id
        , P.message			    as message
        , P.created_date	as created_date
        , 0					    as like_count
        , 0					    as reply_count
        , U.first_name		    as first_name
        , U.last_name		    as last_name
        , U.username		    as username
         FROM post P
        INNER JOIN user U
        ON P.user_id = U.id
        ORDER BY P.created_date desc
        LIMIT %(offset)s, %(limit)s;
        """

        params = {
            "offset": offset,
            "limit": limit
        }

        post_list = []
        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()

            for row in rows:
                post_obj = {
                    "id": row['id'],
                    "message": row['message'],
                    "created_date": str(row['created_date']),
                    "like_count": row['like_count'],
                    "reply_count": row['reply_count'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "username": row['username']
                }

                post_list.append(post_obj)

            return post_list

    def check_like(self, user_id, post_id):
        query = """
        SELECT post_id FROM post_like
        WHERE user_id = %(user_id)s
        AND post_id = %(post_id)s;
        """

        params = {
            "post_id": post_id,
            "user_id": user_id
        }

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, params)
            row = cursor.fetchone()

            if row is not None:
                return True
            else:
                return False

    def add_like(self, user_id, post_id):
        query = """
        INSERT INTO post_like
        (user_id, post_id)
        VALUES
        (%(user_id)s, %(post_id)s);
        """

        params = {
            "post_id": post_id,
            "user_id": user_id
        }

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, params)

    def remove_like(self, user_id, post_id):
        query = """
        DELETE FROM post_like
        WHERE user_id = %(user_id)s
        AND post_id = %(post_id)s;
        """

        params = {
            "post_id": post_id,
            "user_id": user_id
        }

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, params)

    def get_like_count(self, post_id):
        query = """
        SELECT COUNT(*) as count
        FROM post_like
        WHERE post_id = %(post_id)s;
        """

        with self.db.cursor(dictionary=True) as cursor:
            params = {
                "post_id": post_id
            }
            cursor.execute(query, params)
            row = cursor.fetchone()
            count = row['count']

            return count
