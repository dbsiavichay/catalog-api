from abc import ABC, abstractmethod

from .entities import UserCreate


class UserPort(ABC):
    @abstractmethod
    def signup(self, user: UserCreate):
        pass

    @abstractmethod
    def login(self, user: UserCreate):
        pass
