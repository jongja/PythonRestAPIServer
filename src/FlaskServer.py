from flask import Flask, request, jsonify
from src.ServerAdapter import *
import time

class FlaskServer(ServerAdapter):
    __ip : str
    __port : str
    __server : Flask

    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__server = Flask("Server")
        self.__addRules()
    
    def __addRules(self):
        self.__server.add_url_rule('/msg/config', 'get msg', self.__getConfigData, methods=['GET'])
        self.__server.add_url_rule('/file/pfdata', 'get file from client', self.__getPerfettoData, methods=['POST'])

    def __getPerfettoData(self):
        if 'file' not in request.files:
            return jsonify({"message" : "Fail to upload file"})

        file = request.files["file"]
        file.save('./received.txt')

        # Algorithm time
        time.sleep(30)
        
        return jsonify({"message": "File successfully uploaded, file name : {}".format(file.filename)})

    def __getConfigData(self):
        message = request.args.get('pdata')

        data = {
            "msg" : "ACK"
        }

        return jsonify(data)

    def serverStart(self):
        self.__server.run(self.__ip, port=self.__port, debug=True)