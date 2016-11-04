from google.appengine.api import users
from google.appengine.ext import ndb
from models import DB_NAME
from models import db_key
from models import Photo
import webapp2
import jinja2
import json
import os



DEBUG = True



JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'views')),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)



class BaseRequestHandler(webapp2.RequestHandler):
  def generate(self, template_name, template_values={}):
    template = JINJA_ENVIRONMENT.get_template(template_name)
    self.response.out.write(template.render(template_values,
                                            debug=DEBUG))



# handler for "/"
class Upload(BaseRequestHandler):
  def get(self):
    self.generate("upload.html")

  def post(self):
    photo = Photo(parent=db_key(DB_NAME))
    photo.approved = False
    photo.caption = self.request.get('caption')
    photo.file_upload = self.request.get('file-upload')
    photo.put()
    self.redirect('')



# handler for "/photobooth"
class Photobooth(BaseRequestHandler):
  def get(self):
    self.generate("photobooth.html")



# handler for "/api/allapprovedphotos"
class AllApprovedPhotos(BaseRequestHandler):
  def get(self):
    query = Photo.query(Photo.approved == True).order(-Photo.date)
    photos = query.fetch()

    photo_urls = []
    for photo in photos:
      url = "api/photo/%s" % photo.key.urlsafe()
      photo_urls.append(url)

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(photo_urls))



# handler for "/api/photo/..."
class ApiPhoto(BaseRequestHandler):
  def get(self, photo_key):
    key = ndb.Key(urlsafe=photo_key)
    photo = key.get()
    self.response.headers['Content-Type'] = 'image/gif'

    if photo != None:
      self.response.out.write(photo.file_upload)



# handler for "/admin"
class AdminPanel(BaseRequestHandler):
  def get(self):
    is_admin = False
    loginout_url = users.create_login_url(self.request.uri)
    loginout_linktext = 'Login'

    if users.is_current_user_admin():
      is_admin = True
      loginout_url = users.create_logout_url("/")
      loginout_linktext = 'Logout'
    self.generate("admin/panel.html", {
      "IS_ADMIN": is_admin,
      "LOGINOUT_URL": loginout_url,
      "LOGINOUT_LINKTEXT": loginout_linktext,
    })



# handler for "/admin/moderate"
class Moderate(BaseRequestHandler):
  def get(self):
    query = Photo.query(ancestor=db_key(DB_NAME)).order(-Photo.date)
    photos = query.fetch()

    self.generate("admin/moderate.html", {
      "photos": photos,
    })



# handler for "/admin/approve/..."
class Approve(BaseRequestHandler):
  def post(self, photo_key):
    key = ndb.Key(urlsafe=photo_key)
    photo = key.get()
    photo.approved = True
    photo.put()
    self.redirect('/admin/moderate')
