users = {}


def create_user(users):
    username = input("Creá un nombre de usuario: ")
    password = input("Creá una contraseña, debe contener al menos 6 caracteres: ")
    
    while len(password) <6:
        print("La contraseña debe tener al menos 6 caracteres: ")
        password = input("Ingrese una nueva contraseña: ")
        
    users[username] = password
    print(f"Tu usuario fue creado exitosamente!")

create_user(users)


def registered_users(users):
    if users:
        print("Usuarios registrados: ")
        for username in users:
            print(username)
    else:
        print("No hay usuarios registrados")

registered_users(users)


def login(users):
    username = input("Bienvenido/a! Ingresá tu nombre de usuario: ")

    if username not in users:
        print("El usuario no existe")
    else:
        password = input("Ingresá tu contraseña: ")
        registered_password = users[username]
        while registered_password != password:
            password = input("Contraseña incorrecta, vuelve a ingresar tu contraseña: ")
        print(f"Bienvenido/a, {username}!")

login(users)