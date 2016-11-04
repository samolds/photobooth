from google.appengine.ext import ndb


DB_NAME = 'photobooth'


def db_key(db_name=DB_NAME):
  return ndb.Key('Photobooth', db_name)


class Photo(ndb.Model):
  file_upload = ndb.BlobProperty(indexed=False, required=True)
  caption = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)
  approved = ndb.BooleanProperty()
