# -*- coding: utf-8 -*-

#[START imports]
import os
import urllib
import webapp2
#[END imports]


# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        """Return a friendly HTTP greeting."""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('hello, world!')
# [END main_page]


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
# [END app]
