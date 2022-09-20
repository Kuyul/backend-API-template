from webapp.post.dao.dao import PostDAO


class PostService:
    def __init__(self):
        self.dao = PostDAO()

    def share_post(self, user_id: str, message: str):
        post_id = self.dao.share_post(user_id, message)

        return post_id

    def get_newsfeed(self, page: int, limit: int):
        post_list = self.dao.get_newsfeed(page, limit)

        return post_list

    def press_like(self, user_id: str, post_id: str):
        like_pressed = self.dao.check_like(user_id, post_id)

        if like_pressed:
            self.dao.remove_like(user_id, post_id)
        else:
            self.dao.add_like(user_id, post_id)

        like_count = self.dao.get_like_count(post_id)
        return like_count

