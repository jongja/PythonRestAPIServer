from src.NetAPIAdapter import NetAPIAdapter
from src.FlaskAPI import FlaskAPI

if __name__ == '__main__':
    app : NetAPIAdapter
    app = FlaskAPI(["localhost", 34567])
    app.serverRun()