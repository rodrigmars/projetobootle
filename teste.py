from bottle import route, run, template, static_file,get, post, request # or route

usuariosautorizados={"Maria":"mariauser", "João":"joaouser","Antonio":"Antoniouser" }

#@route('/static/<filename>') # rota achar arquivos estaticos
@route('/hello/static/<filename>')
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./views/static')

@get('/login') # or @route('/login')
def login():
  return template('login')


@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username in  usuariosautorizados and password== usuariosautorizados[username]:
        # return "<p>Your login information was correct.</p>"
        @route('/')
        @route('/hello/')
        def hello():
         #return template('Hello {{name}}, how are you?', name=name)
         return template("index")

    else:
        return "<p>Login Falhou</p>"


run(host='localhost', port=8080, debug=True)