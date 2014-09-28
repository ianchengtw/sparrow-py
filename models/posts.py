from google.appengine.ext import db

class Posts(db.Model):
	title = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)

def query_posts():
	posts = db.GqlQuery("SELECT * FROM Posts ORDER BY created DESC")
	return posts

def add_post(title, content):
	p = Posts(title=title, content=content)
	key = p.put()
	return key.id()