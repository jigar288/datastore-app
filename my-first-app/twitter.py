from google.appengine.ext import ndb
from random import randint

class TwitterPost(ndb.Model):
    name = ndb.StringProperty()
    username = ndb.StringProperty()
    retweets = ndb.IntegerProperty()
    comments = ndb.IntegerProperty()
    likes = ndb.IntegerProperty()


name_list = ["josh", "joe", "tim", "john", "jigar"]
username_list = ["joshuser", "joeuser", "timuser", "jigaruser", "jimuser" ]



for i in range(10):
    name_var = name_list[randint(0, len(name_list) - 1)]
    username_var = username_list[randint(0, len(name_list) - 1)]
    post = TwitterPost(name = name_var, username = username_var, retweets = randint(0, 5), comments = randint(0, 5), likes =
    randint(0, 5))
    post.put()

# write a query & print out a data
# field from the results of your query

# use a loop to go over the list of results and print the same field for each of the results
# from twitter import TwitterPost
#
# query = TwitterPost.query(TwitterPost.likes > 1)
#
# list = query.fetch()
#
# for i in range(len(list) - 1):
#     print list[i].likes

#  can also use this for loop
# for results in list:
#     print results.likes


# print all likes greater than 1
#
# from twitter import TwitterPost
#
# query = TwitterPost.query(TwitterPost.likes > 1)
#
# print query.fetch()








#
