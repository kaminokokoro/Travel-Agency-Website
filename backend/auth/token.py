from datetime import datetime, timedelta
from typing import Dict
import jwt
# from jose import jwt
from cryptography.hazmat.primitives.asymmetric import rsa



class AccessToken:
    """ Access Token Util Class"""

    def __init__(self):

        self.__instance=jwt
        self.__algorithm = "RS256"
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()

        self.__signing_key = private_key

        self.__verifying_key = public_key

    def create_access_token(self, *, data: dict,
                            expires_delta: timedelta = None) -> str:
        """Create Access Token Using JWT with RSA256 Encryption"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=15)
        to_encode.update({"ist": int(datetime.now().timestamp())})
        to_encode.update({"exp": (expire)})
        encoded_jwt = self.__instance.encode(to_encode, self.__signing_key,
                                             self.__algorithm)
        return encoded_jwt

    def decode_access_token(self, *, token: str) -> Dict:
        """ Decode Access Token """
        return self.__instance.decode(token, self.__verifying_key,self.__algorithm,
                                      do_time_check=False)


access_token = AccessToken()
# token=access_token.create_access_token(data={"sub": "1234567890"})
#
# print(token)
# print(access_token.decode_access_token(token=token))