from bottle import route, run, template, static_file, get, post, request, response  # or route
import sys
print(">>>>>>>>>>>>>>>", sys.getdefaultencoding())

# usuariosautorizados={"Maria":"mariauser", "João":"joaouser","Antonio":"Antoniouser" }

usuarios_autorizados = [
    {"nome": "Maria", "username": "mariauser", "password": "teste123"},
    {"nome": "João", "username": "João", "password": "teste123"},
    {"nome": "Antonio", "username": "antoniouser", "password": "teste123"}
]


# @route('/static/<filename>') # rota achar arquivos estaticos
# @route('/hello/static/<filename>')
# @route('/static/<filename>')
# def server_static(filename):
#     return static_file(filename, root='./views/static')

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

    print("message 1 ", message)

    try:

        print("request.content_type:", request.content_type)
        print("headers:", request.get_header("origin"))

        username = request.forms.get('username', None)
        password = request.forms.get('password', None)

        print("message 2 ", message)

        if username is None:
            raise Exception("Campo username não informado")

    except Exception as ex:
        message = ex

    else:

        usuario_autenticado = {}

        for usuario in usuarios_autorizados:

            if usuario.get("username") == username and usuario.get("password") == password:
                usuario_autenticado = usuario

                break

        if usuario_autenticado == {}:
            message = "Login Falhou"

        
        print("message 3 ", message)


    finally:

        print("message 4 ", message)

        return template("index") if message is None else f"<p>{message}</p>"


run(host='localhost', port=8080, debug=True)
