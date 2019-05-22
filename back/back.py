import falcon

from resources import UserResource, PostResource, LoginResource, VoteResource

app = falcon.API()

app.add_route("/login", LoginResource())

app.add_route("/user", UserResource())

app.add_route("/post", PostResource())

app.add_route("/vote", VoteResource())