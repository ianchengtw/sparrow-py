import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+'/../templates'),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = JINJA_ENVIRONMENT.get_template(template)
		return t.render(params)

	def render(self, template, *a, **kw):
		self.write(self.render_str(template, **kw))

class MainHandler(Handler):
	def get(self):
		self.render("index.html")
