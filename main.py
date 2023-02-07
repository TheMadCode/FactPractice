from app.Server import Server
from app.modules.core_database import Connector

connection = Connector().get_connection()

serv = Server()
serv.init()