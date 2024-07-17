from abc import ABC, abstractmethod

from .entities import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def retrieve(self, email: str):
        pass
