import web

render=web.template.render('mvc/views/')

class Formulario():
    def GET(self):
        try:
            return render.formulario()
        except Exception as e:
            return "Error "+ str(e.args)