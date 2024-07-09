from abc import *

class ServerAdapter:
    @abstractmethod
    def startServer(self):
        return