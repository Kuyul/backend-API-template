from flask import Blueprint
from flask_restful import Api

posts_blueprint = Blueprint('post', __name__, url_prefix='/api/post')
posts_api = Api(posts_blueprint)
