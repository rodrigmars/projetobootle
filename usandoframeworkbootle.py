from bottle import route, run, template, static_file,get, post, request # or route

usuariosautorizados={"Maria":"mariauser", "João":"joaouser","Antonio":"Antoniouser" }

#@route('/static/<filename>') # rota achar arquivos estaticos
# @route('/hello/static/<filename>')
# @route('/static/<filename>')
# def server_static(filename):
#     return static_file(filename, root='./views/static')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./views/static')

@get('/')
@get('/login') # or @route('/login')
def login():
  return template('login')


@post('/login', method='POST')
def do_login():
        username = request.forms.get('username')
        
        password = request.forms.get('password')

        if username in usuariosautorizados and password == usuariosautorizados[username]:

            return template("index")
          
        else:
            # return template("erro", message="Login Falhou")
            return "<p>Login Falhou</p>"
        
run(host='localhost', port=8080, debug=True)
  

  
                 
#navegador.get("http://localhost:8080/login")
#https://bottlepy.org/docs/dev/tutorial.html#generating-content
#http://localhost:8080/
#http://localhost:8080/hello/ola
