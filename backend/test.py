from datetime import datetime, timedelta
from typing import Dict
from jwt import JWT, jwk_from_pem
from jwt.utils import get_int_from_datetime


class AccessToken:
    """ Access Token Util Class"""

    def __init__(self):

        self.__instance = JWT()
        self.__algorithm = "RS256"
        with open('private_key.pem', 'rb') as fh:
            self.__signing_key = jwk_from_pem(fh.read())
        with open('public_key.pem', 'rb') as fh:
            self.__verifying_key = jwk_from_pem(fh.read())

    def create_access_token(self, *, data: dict,
                            expires_delta: timedelta = None) -> str:
        """Create Access Token Using JWT with RSA256 Encryption"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=15)
        to_encode.update({"ist": get_int_from_datetime(datetime.now())})
        to_encode.update({"exp": get_int_from_datetime(expire)})
        encoded_jwt = self.__instance.encode(to_encode, self.__signing_key,
                                             self.__algorithm)
        return encoded_jwt

    def decode_access_token(self, *, token: str) -> Dict:
        """ Decode Access Token """
        return self.__instance.decode(token, self.__verifying_key,
                                      do_time_check=False)


access_token = AccessToken()
token=access_token.create_access_token(data={"sub": "1234567890"})


print(access_token.decode_access_token(token=token))