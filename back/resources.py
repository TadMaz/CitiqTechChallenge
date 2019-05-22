import falcon
import json

from models import User, Post

class LoginResource():

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))
            
            if User.authenticate(data):
                resp.status_code = 200
            else:
                resp.status_code = 400
        
class UserResource():

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))

            user_dict = User.get_user(data)

            if user_dict is not None:
                resp.body = json.dumps(user_dict)
                resp.status_code = 200
            else:
                resp.status_code = 400

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))
            print(data)

            User.add_user(data)
            resp.status_code = 200       

    def on_delete(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))

            User.delete_user(data)
            resp.status_code = 200 

    def on_put (self, req: falcon.Request, resp: falcon.Response):

        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))

            User.update_user(data)
            resp.status_code = 200 
        

class PostResource():

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))

            post_dict = Post.get_post(data)

            if post_dict is not None:
                resp.body = json.dumps(post_dict)
                resp.status_code = 200
            else:
                resp.status_code = 400


    def on_post(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))

            Post.add_to_DB(data)
            resp.status_code = 200 

    def on_delete(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))

            User.delete_user(data)
            resp.status_code = 200 

class VoteResource():

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))

            votes_dict = Post.get_votecount(data)

            if votes_dict is not None:
                resp.body = json.dumps(votes_dict)
                resp.status_code = 200
            else:
                resp.status_code = 400

         
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        
        if req.content_length:
            data = json.load(req.bounded_stream.read().decode("utf-8"))

            if data["vote"] == "up":
                Post.downvote(data)
                resp.status_code = 200

            elif data["vote"] == "down":
                Post.upvote(data)
                resp.status_code = 200
            
            else: 
                resp.status_code = 400

