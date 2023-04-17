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

# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'cache-control': "no-cache",
#     'Postman-Token': "0c381b9f-58c7-47da-91a8-c98670c0e2f9"
#     }




@post('/login', method='POST')
def do_login():
    
    message = None

    try:

        print("request.content_type:", request.content_type)
        print("headers:", request.get_header("origin"))
        
        # request.content_type.encode("iso-8859-1")

        username = request.forms.get('username', None)
        password = request.forms.get('password', None)

        if username is None:
            raise Exception("Campo username não informado")

    except Exception as ex:
        message = ex

    else:
        print("username:", username.encode)
        print("password:", password)

        usuario_autenticado = {}

        for usuario in usuarios_autorizados:

            if usuario.get("username") == username and usuario.get("password") == password:
                usuario_autenticado = usuario
                
                break
        
        if usuario_autenticado == {}:
            message = "Login Falhou"
    finally:
        template("index") if message is not None  else f"<p>{message}</p>"


run(host='localhost', port=8080, debug=True)


# navegador.get("http://localhost:8080/login")
# https://bottlepy.org/docs/dev/tutorial.html#generating-content
# http://localhost:8080/
# http://localhost:8080/hello/ola
