from flask import Blueprint
from flask_restful import Api
from webapp.post.controller.controller import SharePostController, GetNewsfeedController, PressLikeController

post_blueprint = Blueprint('post', __name__, url_prefix='/api/post')
post_api = Api(post_blueprint)

post_api.add_resource(SharePostController, "/share")
post_api.add_resource(GetNewsfeedController, "/newsfeed")
post_api.add_resource(PressLikeController, "/like")
