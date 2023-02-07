from ._database import Database
from Libs.Design.Patterns import Singleton

@Singleton
class Database_Core(Database):
    __slots__ = [
            'polling', 
    ]

    def __init__(self, database, pool_name):
        super().__init__(database, pool_name)

    def normilize(self, text):
        return text.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

    def ping(self):
        resp = self.call_procedure('ping')
        print(self.normilize(resp[0]["response"]))
        if len(resp) > 0:
            return resp[0]


    def login_by_username(self, username, password):
        resp = self.call_procedure('login_by_username', [username, password])
        if len(resp) > 0:
            return resp[0]

    # name_i text, ufid_i text, relative_filepath_i text, type_i int, extension_i text, timestamp_i int, size_i int
    def add_tracking_files(self, name, ufid, relative_filepath, type, extension, timestamp, alias, size, last_modified):
        resp = self.call_procedure('add_tracking_files', [name, ufid, alias, relative_filepath, type, extension, timestamp, size, last_modified])
        if len(resp) > 0:
            return resp[0]

    def get_ctp_files(self):
        resp = self.call_procedure('get_ctp_files', [])
        if len(resp) > 0:
            return resp

    def request_file(self, ufid):
        resp = self.call_procedure('request_file', [ufid])
        if len(resp) > 0:
            return resp[0]

    # def registration(self, first_name, last_name, second_name, email, phone_number, login, password, user_code):
    #     resp = self.call_procedure('registration', [first_name, last_name, second_name, email, phone_number, login, password, user_code])
    #     if len(resp) > 0:
    #         return resp[0]
        # self.cursor.callproc('registration', [first_name, last_name, second_name, email, phone_number, login, password, user_code])
        # for results in self.cursor.stored_results():
        #     return results.fetchall()[0]

    def add_user(self, uuid_i, name_i, surname_i, middle_name_i, login_i, password_i, role_i):
        try:
            resp = self.call_procedure('add_user', [uuid_i, name_i, surname_i, middle_name_i, login_i, password_i, role_i])
            if len(resp) > 0:
                return resp[0]
        except:
            return {"code": 300, "response": "user already exists"}


    def get_user_by_uuid(self, user_uuid):
        resp = self.call_procedure('get_user_by_uuid', [user_uuid])
        if len(resp) > 0:
            return resp[0]

@Singleton
class Connector:
    def __init__(self) -> None:
        try:
            self.connection = Database_Core(database="vermucht", pool_name="db_vermucht")

        except:
            self.connection = None

    def get_connection(self):
        return self.connection