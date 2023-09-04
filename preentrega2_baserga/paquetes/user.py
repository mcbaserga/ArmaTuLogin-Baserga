import random


class User:
    def __init__(self, name, email, username, password):
        self.id = self.generate_id()
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        return f"El mail ingresado {self.email} corresponde al usuario {self.username} con id {self.id}"

    def generate_id(self):
        return random.randint(1000, 9999)
