from google.appengine.ext import ndb
from post import Post

class User(ndb.Model):
    username = ndb.StringProperty()
    bio = ndb.StringProperty()
    post1 = ndb.KeyProperty(Post)
    # post1 = ndb.KeyProperty(Post, repeated = True)
    following = ndb.StringProperty('User', repeated = True)
