import jwt
from datetime import datetime, timezone, timedelta
from Domain.Ports.Security.token_service_interface import TokenServiceInterface
from Domain.settings import settings


class JwtServices(TokenServiceInterface):

    def create_access_token(self, data):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire, "type": "access"})
        return jwt.encode(to_encode, settings.ACCESS_TOKEN_SECRET, algorithm=settings.JWT_ALGORITHM)


    def create_refresh_token(self, data):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire, "type": "refresh"})
        return jwt.encode(to_encode, settings.REFRESH_TOKEN_SECRET, algorithm=settings.JWT_ALGORITHM)
    


    def verify_token(self, token: str, token_type: str) -> dict:
        secret = settings.ACCESS_TOKEN_SECRET if token_type == "access" else settings.REFRESH_TOKEN_SECRET
        try:
            payload = jwt.decode(token, secret, algorithms=[settings.JWT_ALGORITHM])
            if payload.get("type") != token_type:
                raise ValueError(f"Invalid token type. Expected {token_type} token.")
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token is expired.")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token.")
        

        
    def is_token_expired(self, token: str, token_type: str) -> bool:
        secret = settings.ACCESS_TOKEN_SECRET if token_type == "access" else settings.REFRESH_TOKEN_SECRET
        try:
            payload = jwt.decode(token, secret, algorithms=[settings.JWT_ALGORITHM], options={"verify_exp": False})
            exp_timestamp = payload.get("exp")
            if exp_timestamp is None:
                return True
            expiration = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
            now = datetime.now(timezone.utc)

            return now > expiration

        except jwt.InvalidTokenError:
            return True