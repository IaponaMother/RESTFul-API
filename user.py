import requests
import json
class User:
    def __init__(self,id, username, firstName, lastName, email, password, phone, userStatus):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus
        self.d = {"id": self.id, "username": self.username, 'firstName': self.firstName, 'lastName': self.lastName,
             'email': self.email, 'password': self.password, 'phone': self.phone, 'userStatus': self.userStatus}

    def dict_format(self, json_string):
        self.json_string = json_string
        return json.load(self.json_string)

    def __str__(self):
        return json.dumps(self.d, indent=4)


u = User(0, 'MkrtchyanKarina', 'Karina', 'Mkrtchyan', 'mkrtchyan.karina@mail.ru', '123456', '12345678', 666 )

print(u)
