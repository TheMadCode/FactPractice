from enum import Enum
from app.Libs.Design.Patterns import Singleton
from app.modules.core_database import Connector

import functools

@Singleton
class Groups:
    def __init__(self) -> None:
        self.connection = Connector().get_connection()

    def get(self):
        return self.connection.get_groups()

@Singleton
class People:
    class Actions(Enum):
        Remove = 0x01
        Create = 0x02
        Edit =  0x03

    def __init__(self) -> None:
        self.connection = Connector().get_connection()

    def get_people(self):
        return self.connection.get_people()

    def update_person(self, name, surname, middle_name, birth_date, average_mark, uuid, group, study_year):
        '''
            TODO: Insert required data
        '''
        return self.connection.update_person(
            name=name,
            surname=surname,
            middle_name=middle_name,
            birth_date=birth_date,
            average_mark=average_mark,
            uuid=uuid,
            group=group,
            study_year=study_year
        )

    def remove_person(self, data):
        '''
            uuid required
        '''
        return self.connection.remove_person(data['uuid'])

    def add_person(self, data):
        '''
            name, surname, middle_name, birth_date, average_mark, uuid
        '''
        return self.connection.add_person(
            name=data['name'],
            surname=data['surname'],
            middle_name=data['middleName'],
            birth_date=None,
            average_mark=data['GCA'],
            uuid=data['uuid'],
            group=data['group'],
            study_year=data['study_year']
        )

    # def __filter_by_operation(*elem, **kwargs):
    #     print(elem)

    def save_changes(self, actions):

        def perform_operation(operation):
            def decorator(func):
                
                def wrapper(elem):
                    return filter_by_operation(elem, operation.value)

                return wrapper

            return decorator

        def filter_by_operation(elem, operation):
            if (elem['action'] == operation):
                return True
            else:
                return False

        @perform_operation(self.Actions.Remove)
        def get_delete_actions(self, elem):
            ''' Syntax sugar '''
            pass

        @perform_operation(self.Actions.Create)
        def get_create_actions(elem):
            ''' Syntax sugar '''
            pass

        @perform_operation(self.Actions.Edit)
        def get_update_actions(elem):
            ''' Syntax sugar '''
            pass

        create_actions = list(filter(get_create_actions, actions))
        update_actions = list(filter(get_update_actions, actions))
        delete_actions = list(filter(get_delete_actions, actions))

        # print(create_actions)
        # print(update_actions)
        # print(delete_actions)

        #create 
        for action in create_actions:
            self.add_person(
                name=action['entity']['name'],
                surname=action['entity']['surname'],
                middle_name=action['entity']['middle_name'],
                birth_date=action['entity']['birth_date'].split("T")[0],
                average_mark=action['entity']['average_mark'],
                uuid=action['entity']['uuid'],
                group=action['entity']['group'],
                study_year=action['entity']['study_year']
            )

        #update
        for action in update_actions:
            self.update_person(
                name=action['entity']['name'],
                surname=action['entity']['surname'],
                middle_name=action['entity']['middle_name'],
                birth_date=action['entity']['birth_date'].split("T")[0],
                average_mark=action['entity']['average_mark'],
                uuid=action['entity']['uuid'],
                group=action['entity']['group'],
                study_year=action['entity']['study_year']
            )

        #delete
        for action in delete_actions:
            self.remove_person(
                uuid=action['item'],
            )