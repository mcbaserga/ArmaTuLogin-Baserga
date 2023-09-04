from paquetes.user import User
import json


def create_user():
    name = input("Ingresá tu nombre: ")
    email = input("Ingresá tu email: ")
    username = input("Elegí un nombre de usuario: ")
    password = input("Creá una contraseña: ")
    while len(password) <6:
        print("La contraseña debe tener al menos 6 caracteres: ")
        password = input("Ingrese una nueva contraseña: ")

    return User(name, email, username, password)

def save_user_to_json(user, filename):
    user_data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'username': user.username,
        'password': user.password
    }
    with open(filename, 'w') as file:
        json.dump(user_data, file, indent=4)

def create_json():
    user = create_user()
    filename = f"{user.username}.json" 
    save_user_to_json(user, filename)
    print("Usuario creado como", filename)
    
create_json()