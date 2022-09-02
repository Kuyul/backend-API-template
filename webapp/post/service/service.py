from webapp.post.dao.dao import PostDAO


class PostService:
    def __init__(self):
        self.dao = PostDAO()
