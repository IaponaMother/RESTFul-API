import requests
import json
users = []

class User:
    result = ''

    def __init__(self, *user_data):

        if len(user_data) == 1:
            global result
            result = json.loads(user_data[0])
        else:
            self.id = user_data[0]
            self.username = user_data[1]
            self.firstName = user_data[2]
            self.lastName = user_data[3]
            self.email = user_data[4]
            self.password = user_data[5]
            self.phone = user_data[6]
            self.userStatus = user_data[7]
            self.d = {"id": self.id, "username": self.username, 'firstName': self.firstName, 'lastName': self.lastName,
                      'email': self.email, 'password': self.password, 'phone': self.phone,
                      'userStatus': self.userStatus}

            result = json.dumps(self.d, indent=4)

    def print_res(self):
        return result


u1 = User(0, 'MkrtchyanKarina', 'Karina', 'Mkrtchyan', 'mkrtchyan.karina@mail.ru', '123456', '12345678', 666).print_res()
u2 = User('{"id": 6, "username": "Andrey"}').print_res()

print(u1)
users.append(str(u1))
print(u2)
users.append(str(u2))

class Request:
    def get(self, username):
        if username == '':
            return users
        else:
            return users[users.index(username)]

    def delete(self, username):
        del users[users.index(username)]
        return users

    def put(self, username, new_str):
        users[users.index(username)] = new_str
        return users

    def post(self, username):
        users.append(username)
        return users

r = Request()
r.post('new user')
print(users)
