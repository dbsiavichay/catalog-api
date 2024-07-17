from abc import ABC, abstractmethod

from .entities import Email


class EmailPort(ABC):
    @abstractmethod
    def send_email(self, email: Email):
        pass
