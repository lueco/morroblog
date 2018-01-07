import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext.webapp import template


class Post(webapp.RequestHandler):
    def get(self, *ar, **kw):
        index_path = iteratePath(ar[0])
        try:
            if isPost(index_path):
                path = os.path.join(os.path.dirname(__file__), '_site/' + index_path + '.html')
            else:
                path = os.path.join(os.path.dirname(__file__), '_site/' + index_path + '/index.html')
            self.response.out.write(template.render(path, {}))
        except:
            path = os.path.join(os.path.dirname(__file__), '_site/error.html')
            self.response.out.write(template.render(path, {}))


def iteratePath(path):
    while str(path).endswith("/"):
        path = path[0:(len(path) - 1)]
    return path


def isPost(path):
    return str(path).startswith("posts/")


run_wsgi_app(webapp.WSGIApplication(
        [
            (r'/(.*)', Post),
        ]
        ,
        debug=True))

