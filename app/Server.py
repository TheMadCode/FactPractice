import json

from datetime import timedelta

from flask import Flask, render_template, make_response, request, jsonify, redirect
from flask_jwt import JWT, jwt_required, current_identity
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from werkzeug.security import safe_str_cmp

from engineio.payload import Payload

from .Libs.Outputer.logger import print, LoggerColor

from .modules.connection import Connection
from .modules.dataset import Accounts, LoginCredentials, Users

import eventlet
eventlet.monkey_patch(thread=False)

Payload.max_decode_packets = 99999999999999999999

class Server:
    def __init__(self) -> None:
        if __name__ == "__main__":
            self.app = Flask(__name__)

        else:
            self.app = Flask(__name__, static_url_path='/app/')
        
        with open("./set_up.json", "r") as f:
            data = json.load(f)

        self.app.secret_key = data['secret_key']
        self.app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=160)

        self.socketio = SocketIO(self.app)

        self.users_dataset = Users()
        self.username_dataset = LoginCredentials(self.users_dataset.get_users())
        self.userid_dataset = Accounts(self.users_dataset.get_users())

        self.jwt = JWT(self.app, self.authenticate, self.identity)

    def authenticate(self, username, password):
        if self.username_dataset.validate(username, password)[0]:
            return self.userid_dataset.get(username)

    def identity(self, payload):
        user_id = payload['identity']
        return self.userid_dataset.get_by_id(user_id)

    def init_routes(self):
        @self.app.route("/")
        def index():
            return redirect("/logger", code=302)

        # @self.app.route("/auth", methods=["GET"])
        # def auth():
        #     # print(current_identity)
        #     return render_template("./auth.html")

        @self.app.route("/human.api/get_human", methods=['GET'])
        def get_humans():
            return "Implementation Error", 500

        @self.app.route("/human.api/add_human", methods=['POST'])
        def add_humans():
            return "Implementation Error", 500
            
        @self.app.route("/human.api/remove_human", methods=['POST'])
        def remove_humans():
            return "Implementation Error", 500

        @self.app.route("/human.api/update_human", methods=['POST'])
        def update_humans():
            return "Implementation Error", 500

        @self.app.route("/logger/get_logs", methods=["GET"])
        def get_logger():
            return print()
            

        @self.app.route("/logger", methods=["GET"])
        def logger():
            # if isLoggingOnServer():
            return render_template("./logger.html", loggs=print())

        @self.app.route("/i0saf2i0g2i02di07hdqQ2h79q3sjf089", methods=["GET"])
        def shutdown():
            self.socketio.stop()
            return "Shutting down..."
        
        @self.socketio.on('connect')
        @jwt_required()
        def connect(sid):
            self.current_user_sid = request.sid
            # print(current_identity)
            # print(f"connected {current_identity.username}")
            current_identity.set_connection(Connection(current_identity))
            join_room(current_identity.get_connection().get_room())
            emit("Hello", {"data": "Hello"}, room=current_identity.get_connection().get_room())
 
        # @self.socketio.on("info")
        # @jwt_required()
        # def response(data):
        #     # print(current_identity.get_connection().get_room())
        #     if self.manager.get_status() == States.IN_GAME:
        #         emit("info", {"speed": self.manager.get_speed(), "gear": self.manager.get_gear(), "RPM": self.manager.get_rpm()}, room=current_identity.get_connection().get_room())
        #     else:
        #         emit("info", {"status": self.__get_status__()})

        # @self.socketio.on('connect_to_logs')
        # def connect_to_logs(data):
        #     print(data, type=LoggerColor.warn)
        #     # emit("Hello", {"data": "Hello"}, room=current_identity.get_connection().get_room())

    
    def init(self):
        self.init_routes()
        print("[+] Server initialized.", type=LoggerColor.GREEN)
        self.socketio.run(self.app, host="0.0.0.0", port="5050")