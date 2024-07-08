from abc import *

class NetAPIAdapter:
    @abstractmethod
    def sendMessage(self, msg : str):
        return True

    @abstractmethod
    def getMessage(self):
        return str

    @abstractmethod
    def getFile(self, path : str):
        return 0

    @abstractmethod
    def sendFile(self, path :str):
        return True

    @abstractmethod
    def serverRun(self):
        return