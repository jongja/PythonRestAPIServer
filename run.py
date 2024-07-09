from src.FlaskServer import *

if __name__ == '__main__':
    app = FlaskServer("localhost", 34567)
    app.serverStart()