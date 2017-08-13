from google.appengine.ext import ndb
from user import User


class Post(ndb.Model):
    image = ndb.BlobProperty()
    description = ndb.StringProperty()
    
