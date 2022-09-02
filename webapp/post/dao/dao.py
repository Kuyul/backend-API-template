from common_lib.infra.mysql import DB
from uuid import uuid4


class PostDAO:
    def __init__(self):
        self.db = DB()
