import webapp2
import controllers


app = webapp2.WSGIApplication([
  webapp2.Route(r'/', controllers.Upload),
  webapp2.Route(r'/photobooth', controllers.Photobooth),
  webapp2.Route(r'/api/allapprovedphotos', controllers.AllApprovedPhotos),
  webapp2.Route(r'/api/photo/<photo_key:[A-Za-z0-9_\-]+$>', controllers.ApiPhoto),

  webapp2.Route(r'/admin', controllers.AdminPanel),
  webapp2.Route(r'/admin/moderate', controllers.Moderate),
  webapp2.Route(r'/admin/approve/<photo_key:[A-Za-z0-9_\-]+$>', controllers.Approve),
], debug=controllers.DEBUG)
