import web

urls = (
    '/', 'mvc.controller.formulario.Formulario'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()