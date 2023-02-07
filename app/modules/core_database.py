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

    def add_person(self, name, surname, middle_name, uuid, birth_date):
        resp = self.call_procedure('add_person', [name, surname, middle_name, birth_date, uuid])
        if len(resp) > 0:
            return resp[0]

    def update_person(self, name, surname, middle_name, uuid, birth_date):
        resp = self.call_procedure('update_person', [name, surname, middle_name, birth_date, uuid])
        if len(resp) > 0:
            return resp[0]

    def remove_person(self, uuid):
        resp = self.call_procedure('remove_person', [uuid])
        if len(resp) > 0:
            return resp[0]

    def get_people(self):
        resp = self.call_procedure('get_people', [])
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