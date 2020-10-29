from abc import ABCMeta, abstractmethod


class CredentialFacade(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getLogin(self):
        pass
