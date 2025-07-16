from typing import Optional

class DTO_LoginResponse:
    def __init__(self, access_token: str, refresh_token: str, user_data: dict):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.user_data = user_data

    def to_dict(self):
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "user_data": self.user_data
        }