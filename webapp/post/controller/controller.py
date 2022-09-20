from flask.views import MethodView
from flask import request
from webapp.post.service.service import PostService
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


class SharePostController(MethodView):
    def __init__(self):
        self.service = PostService()

    @jwt_required()  # This declares that this method can only be called with a JWT token
    def post(self):
        input_data = request.get_json()
        message = input_data['message']  # Post message is stored in the "message" field
        user_id = get_jwt_identity()  # JWT token contains the user id as identity.
        post_id = self.service.share_post(user_id, message)  # Service logic not implemented yet, but we know what values we pass in, and what values to get back

        return {
            "data": {
                "post_id": post_id
            },
            "error": None,
            "status": "success"
        }


class GetNewsfeedController(MethodView):
    def __init__(self):
        self.service = PostService()

    @jwt_required()
    def get(self):
        page = int(request.args.get('page'))
        limit = int(request.args.get('limit'))

        post_list = self.service.get_newsfeed(page, limit)

        return {
            "data": {
                "posts": post_list
            },
            "error": None,
            "status": "success"
        }


class PressLikeController(MethodView):
    def __init__(self):
        self.service = PostService()

    @jwt_required()
    def post(self):
        input_data = request.get_json()
        post_id = input_data['post_id']
        user_id = get_jwt_identity()

        new_like_count = self.service.press_like(user_id, post_id)

        return {
            "data": {
                "like_count": new_like_count
            },
            "error": None,
            "status": "success"
        }
