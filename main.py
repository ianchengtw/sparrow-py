import webapp2
from handler import *


# URI routing
app = webapp2.WSGIApplication([
	('/', handler.MainHandler),
	('/posts', posts.PostsHandler),
	('/newpost', posts.NewPostHandler),
	('/post/(\d+)', posts.Permalink),
], debug=True)
