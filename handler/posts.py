from handler import Handler
from model import posts
from time import sleep

class PostsHandler(Handler):
	def get(self):
		data = posts.query_posts()
		self.render("posts.html", data=data)

class NewPostHandler(Handler):
	def get(self):
		self.render("new_post.html")

	def post(self):
		title = self.request.get('title')
		content = self.request.get('content')

		if title and content:
			content = content.replace("\n", "<br>")
			record_id = posts.add_post(title, content)

			sleep(1)

			self.redirect('/post/%d' % record_id)
		else:
			data = { "error": "We need both Title and Content!" }
			self.render("new_post.html", data=data)

class Permalink(Handler):
	def get(self, post_id):
		post = posts.Posts.get_by_id(int(post_id))
		self.render("posts.html", data=[post])



