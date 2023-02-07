import time

from app.Libs.Design.Patterns import Singleton

from ..modules.Error_Codes import Error_Codes

class User(object):
    def __init__(self, id, uname, password) -> None:
        self.id = id
        self.username = uname
        self.password = password
        self.connection = None

    def set_connection(self, conn):
        self.connection = conn

    def get_connection(self):
        return self.connection

    # def __getattribute__(self, item):
    #     print(item)
    #     time.sleep(2)
    #     print(item)
    #     print(item)
    #     return object.__getattribute__(self, item)

    def __str__(self):
        return "User(id='%s')" % self.id

@Singleton
class Users:
    def __init__(self) -> None:
        self.users = [
            User(1, "user0", '000')
        ]

    def get_users(self):
        return self.users

@Singleton
class LoginCredentials:
    def __init__(self, userList) -> None:
        self.__usernames_passwords__ = self.__get_login_pass__(userList)
        # self.__usernames_passwords__ = {
        #     "user0": "000"
        # }

    def __get_login_pass__(self, userList):
        user_pass = {}

        for user in userList:
            user_pass[user.username] = user.password

        return user_pass

    def validate(self, login, password):
        if login.lower() in self.__usernames_passwords__.keys():
            if password == self.__usernames_passwords__[login]:
                return True, "Success"
            
            else:
                return False, Error_Codes.incorrect_password
        
        else:
            return False, Error_Codes.incorrect_login

@Singleton
class Accounts:
    def __init__(self, userList) -> None:
        self.__users__ = self.__get_users_ids__(userList)

    def __get_users_ids__(self, userList):
        user_ids = {}

        for user in userList:
            user_ids[user.username] = user

        return user_ids

    def get(self, username):
        return self.__users__[username]

    def get_by_id(self, user_id):
        for usr in self.__users__.values():
            if usr.id == int(user_id):
                return usr
