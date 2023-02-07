from enum import Enum

class Error_Codes(Enum):
    incorrect_password = 0x01
    incorrect_login = 0x02
    incorrect_token = 0x03
    incorrect_login_data = 0x04