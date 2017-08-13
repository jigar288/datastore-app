#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import urllib2
import urllib
import jinja2
import json
from random import randint
import os
import webapp2
from google.appengine.ext import ndb
from snack import Snack
from random import choice
from google.appengine.api import users




jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def stuff(self, name):
        groceries = ["milk", "cheese", "bread", "fruits"]
        return groceries[2] + " " + name
    def get(self):
        response = self.stuff("matthew")
        self.response.write(response)

class FruitHandler(webapp2.RequestHandler):
    greetings = ["yo", "hi", "hello"]
    def get(self):
        self.response.write(self.greetings[0])

class MilkHandler(webapp2.RequestHandler):
    def get(self):
        produce_name = self.request.get("produce")
        self.response.write("Go get some milk!! & " + produce_name)

class SportHandler(webapp2.RequestHandler):
    def get(self):
        sport_name = self.request.get("sport")
        sport_number = int(self.request.get("number"))
        self.response.write(sport_name * sport_number)


class ImageHandler(webapp2.RequestHandler):
    def get(self):
        greetinglist = ["yo", "hi", "hello"]
        name_value = self.request.get("my_name")
        if name_value== "":
            name_value = 'nothing entered'
        my_template = jinja_environment.get_template("templates/hello-world.html")
        render_data = {
        'greeting' : greetinglist[randint(0, 2)],
        'name_entered': name_value,
        'fav_color': self.request.get("fav_color"),
        'rnumber': int(self.request.get("rnumber"))
        }
        # self.response.write("<link rel='stylesheet' href='resources/file.css'>")
        # self.response.write("<h4>")
        # self.response.write("works")
        # self.response.write("</h4>")
        # self.response.write("<img src='resources/milk.jpg'>")
        self.response.write(my_template.render(render_data))


# class SportHandler(webapp2.RequestHandler):
#     def get(self):
#         sport_name = self.request.get("sport")
#         sport_number = int(self.request.get("number"))

#         self.response.write(sport_name * sport_number)

class GifHandler(webapp2.RequestHandler):
    def get(self):
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': 'puppy', 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
        giphy_data_source = urllib2.urlopen(
            "http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
        giphy_json_content = giphy_data_source.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        self.response.write("<img src=" + (gif_url)+ '>')


class SnackHandler(webapp2.RequestHandler):
    def get(self):
        snack_value = self.request.get("my_snack")
        rating_value = int(self.request.get("my_rating") or 1)
        quantity_value = int(self.request.get("my_quantity") or 1)
        calories_value = int(self.request.get("my_calories") or 1)
        my_template = jinja_environment.get_template("templates/hello-world.html")
        my_snack_variable = Snack(kind = snack_value, rating = rating_value, quantity = quantity_value, calories= calories_value)
        my_snack_variable.put()
        self.response.write(my_template.render())

class SnackPrintHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/hello-world.html")
        getList = self.request.get("getList")
        render_data = {}
        query = Snack.query()
        render_data["getList"] = query.fetch()
        self.response.write(template.render(render_data))
        for results in query:
            kind = "<br/>" + results.kind




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/milk', MilkHandler),
    ('/fruit', FruitHandler),
    ('/play', SportHandler),
    ('/image', ImageHandler),
    ('/gif', GifHandler),
    ('/snack', SnackHandler),
    ('/snackprint', SnackPrintHandler)

], debug=True)



# Get user input from the cgi args and
