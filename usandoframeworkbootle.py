from bottle import route, run, template, static_file, get, post, request, response  # or route
import sys
print(">>>>>>>>>>>>>>>", sys.getdefaultencoding())

# usuariosautorizados={"Maria":"mariauser", "João":"joaouser","Antonio":"Antoniouser" }

usuarios_autorizados = [
    {"nome": "Maria", "username": "mariauser", "password": "teste123"},
    {"nome": "João", "username": "João", "password": "teste123"},
    {"nome": "Antonio", "username": "antoniouser", "password": "teste123"}
]


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./views/static')


@get('/')
@get('/login')  # or @route('/login')
def login():
  return template('login')


@post('/login', method='POST')
def do_login():

    message = None

    try:

        username = request.forms.get('username', None)
        password = request.forms.get('password', None)

        if username is None:
            raise Exception("Campo username não informado")

    except Exception as ex:
        message = ex

    else:

        usuario_autenticado = {}

        for usuario in usuarios_autorizados:

            if usuario.get("username") == username and usuario.get("password") == password:

                usuario_autenticado["username"] = usuario["username"]
                usuario_autenticado["nome"] = usuario["nome"]

                break

        if usuario_autenticado == {}:
            message = "Login Falhou"

    finally:

        return template("index", usuario_autenticado) if message is None else template("erro", message)


run(host='localhost', port=8080, debug=True)
