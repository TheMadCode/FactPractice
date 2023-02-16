from app.Libs.Design.Patterns import Singleton
from ._database import Database
from datetime import date

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

    def add_person(self, name, surname, middle_name, uuid, average_mark, birth_date, group, study_year):
        resp = self.call_procedure('add_person', [name, surname, middle_name, average_mark, uuid, birth_date, group, study_year])
        if len(resp) > 0:
            return resp[0]

    def update_person(self, name, surname, middle_name, uuid, average_mark, birth_date, group, study_year):
        resp = self.call_procedure('update_person', [uuid, name, surname, middle_name, average_mark, birth_date, group, study_year])
        if len(resp) > 0:
            return resp[0]

    def remove_person(self, uuid):
        resp = self.call_procedure('remove_person', [uuid])
        if len(resp) > 0:
            return resp[0]

    def get_people(self):
        resp = self.call_procedure('get_people', [])
        for item in resp:
            if item['birth_date'] != None:
                item['birth_date'] = item['birth_date'].isoformat()
        if len(resp) > 0:
            return resp

    def get_groups(self):
        resp = self.call_procedure('get_groups', [])
        if len(resp) > 0:
            return resp

@Singleton
class Connector:
    def __init__(self) -> None:
        try:
            self.connection = Database_Core(database="fact_test", pool_name="db_fact")

        except:
            self.connection = None

    def get_connection(self):
        return self.connection