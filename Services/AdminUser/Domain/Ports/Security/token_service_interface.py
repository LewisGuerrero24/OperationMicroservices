from abc import ABC, abstractmethod

class TokenServiceInterface(ABC):

    @abstractmethod
    def create_access_token(self, data: dict) -> str:
        pass

    @abstractmethod
    def create_refresh_token(self, data: dict) -> str:
        pass

    @abstractmethod
    def verify_token(self, token: str, token_type: str) -> dict:
        pass

    @abstractmethod
    def is_token_expired(self, token: str, token_type: str) -> bool:
        pass