from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
#import wsgiref.handlers

class MainPage(webapp.RequestHandler):
    def get(self):

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('If you wanna contact me, mail to kyan.ql.he@gmail.com')

# RFC Page has 56 lines
RFC_PAGE_SIZE = 56
class Convert(webapp.RequestHandler):
    def w(self, s):
        self.response.out.write(s)

    def get(self):

        self.w("""
<html>
<head>
<link type="text/css" rel="stylesheet" href="http://www.gstatic.com/codesite/ph/6142392302819995991/css/d_sb.css" >
<link type="text/css" rel="stylesheet" href="http://www.gstatic.com/codesite/ph/6142392302819995991/css/ph_detail.css" >
</head>
<body>
""")

        self.w('<pre class="prettyprint"><table>\n')

        f = open('rfc3261.txt', 'r')

        # skip first padding line
        f.readline()

        page = 0
        # in order to break the outmost loop
        line = ""
        while True:
            for i in range(RFC_PAGE_SIZE):
                line = f.readline()

                if not line:
                    break;
                self.w('<tr><td>%d</td><td class="source">%s</td></tr>' % (page*RFC_PAGE_SIZE + 1 + i, line))

            page = page + 1
            if not line:
                break;
        self.w('</pre></table></body></html>')

application = webapp.WSGIApplication([
    ('/c', Convert),
    ('/.*', MainPage)],debug=True)

def main():
    run_wsgi_app(application)
    #wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
