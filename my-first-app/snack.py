from google.appengine.ext import ndb


# kinds (str), rating (int), quantity (int), calories (int), expiration (date)

#make it so that users can add data to datastore with cgi args
#stretch is to do a form

class Snack(ndb.Model):
    kind = ndb.StringProperty(required = True)
    rating = ndb.IntegerProperty()
    quantity = ndb.IntegerProperty()
    calories = ndb.IntegerProperty()
    expiration = ndb.DateProperty()

# kinds (str), rating (int), quantity (int), calories (int), expiration (date)

#make it so that users can add data to datastore with cgi args
#stretch is to do a form

#make a request to display snacks to fetch all snacks from datastore

# create two models for a instagram type app
# the first model is a user , which has a username and a description or bio 
