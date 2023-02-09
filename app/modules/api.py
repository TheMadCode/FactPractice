from app.Libs.Design.Patterns import Singleton
from app.modules.core_database import Connector


@Singleton
class People:
    def __init__(self) -> None:
        self.connection = Connector().get_connection()

    def get_people(self):
        return self.connection.get_people()

    def update_person(self, name, surname, middle_name, birth_date, average_mark, uuid):
        '''
            TODO: Insert required data
        '''
        return self.connection.update_person(
            name=name,
            surname=surname,
            middle_name=middle_name,
            birth_date=birth_date,
            average_mark=average_mark,
            uuid=uuid
        )

    def remove_person(self, uuid):
        '''
            uuid required
        '''
        return self.connection.remove_person(uuid)

    def add_person(self, name, surname, middle_name, birth_date, average_mark, uuid):
        '''
            name, surname, middle_name, birth_date, average_mark, uuid
        '''
        return self.connection.add_person(
            name=name,
            surname=surname,
            middle_name=middle_name,
            birth_date=birth_date,
            average_mark=average_mark,
            uuid=uuid
        )
