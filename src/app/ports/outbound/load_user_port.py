from abc import ABC, abstractmethod


class LoadUserPort(ABC):
    # TODO: Add type annotations
    @abstractmethod
    def loadUser(credentials):
        pass
