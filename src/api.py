from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from utils.constants import VALID_SORT_VALUES, VALID_DIRECTION_VALUES
from services.blog import Blog
from functools import lru_cache



route1 = "/api/ping"
route2 = "/api/posts"

# Application factory
def create_app(test_config=None):
    app = Flask(__name__)

    api = Api(app)

    #error handlers
    @app.errorhandler(400)
    def resource_not_found(e):
        return jsonify(error=str(e)), 400

    @app.errorhandler(500)
    def resource_internal_error(e):
        return jsonify(error=str(e)), 500

    @app.errorhandler(404)
    def requested_method_not_found(error):
        error_message = (
            "The server can not find requested resource. "
            "The endpoint may be valid but the resource itself does not exist."
        )
        return jsonify(error= error_message), 404

    class Ping(Resource):
        #Route 1
        def get(self):
            return jsonify(success=True)

    class Blogger(Resource):
        #Route 2
        @lru_cache
        def get(self):
            sortBy=request.args.get('sortBy',default = "", type = str)
            direction=request.args.get('direction',default = "", type = str)
            blogs=[]
            tags=request.args.get('tags', default = "", type = str)

            if tags=="":
                return resource_not_found("Tags parameter is required")

            if len(tags.split(','))==0:
                return resource_not_found("Tags parameter is required")
            
            if sortBy!="" and (sortBy not in VALID_SORT_VALUES):
                if direction!="" and (direction not in VALID_DIRECTION_VALUES):
                    return resource_not_found("direction parameter is required")
                return resource_not_found("sortBy parameter is required")
                
                        
            tags=request.args.get('tags')
            reader=Blog()

            blogs = reader.get_posts(tags_string=tags, sortBy=sortBy, direction=direction)

            
            
            return jsonify(posts=blogs)
    
    api.add_resource(Ping, route1)
    api.add_resource(Blogger, route2)

    return app


