import web
render = web.template.render('templates/')
urls = (
    '/(.*)','index'
)

class index:
    """docstring for."""
    def GET(self,name):
        i=web.input(name = None)
        return render.index(name)
        #return "Hello World!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
