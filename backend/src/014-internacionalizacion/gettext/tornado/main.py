import tornado.ioloop
import tornado.web
import tornado.locale

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        _ = self.locale.translate

        # Mostrar las localizaciones soportadas
        print( tornado.locale.get_supported_locales() )

        self.render("home.html", text=_("Hello, world!"))

application = tornado.web.Application([
    tornado.web.url(r"/", HomeHandler, name='home'),
])

if __name__ == "__main__":
    # Cargar todas las traducciones de gettext: (dir, domain)
    tornado.locale.load_gettext_translations('locale', 'messages')

    # Establecer localización por defecto
    tornado.locale.set_default_locale("ru-RU")

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
