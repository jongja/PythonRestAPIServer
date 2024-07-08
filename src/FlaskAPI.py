from flask import Flask, request, jsonify
from src.NetAPIAdapter import *

class FlaskAPI(NetAPIAdapter):
    __host_ip : str
    __host_port : str
    __server : Flask
    def __init__(self, host_info : list):
        ip, port = host_info
        self.__host_ip = ip
        self.__host_port = port
        self.__server = Flask("Server")
        self.__server.add_url_rule('/api/msg', 'get msg', self.getMessage, methods=['GET'])

    def sendMessage(self, msg : str):
        return True

    def getMessage(self):
        message = request.args.get('pdata')

        data = {
            "msg" : "ACK"
        }

        return jsonify(data)

    def getFile(self, path : str):
        return 0

    def sendFile(self, path :str):
        return True

    def serverRun(self):
        self.__server.run(self.__host_ip, port=self.__host_port, debug=True)