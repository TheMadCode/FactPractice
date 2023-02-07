import jwt
from .dataset import User

# def validation(_user):
#     pass

class Connection:
    def __init__(self, current_identity) -> None:
        self.__current_identity__ = current_identity
        self.room = f"room_[id:{current_identity.id}_UName:{current_identity.username}]"

    def get_room(self):
        return self.room