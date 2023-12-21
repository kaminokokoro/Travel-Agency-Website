from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi.responses import JSONResponse
from backend.crud.CRUDUser import crud_user
from backend.auth.token import access_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"getToken")

def get_current_user(token: str = Depends(oauth2_scheme)) -> JSONResponse:
    """ Return Current User"""
    try:
        payload = access_token.decode_access_token(token=token)
        print(payload)
        user = crud_user.get_user_by_phone_number(phone_number=payload.get("sub"))
        if user is None:
            raise HTTPException(status_code=401,
                                detail="Unauthorized")
        else:
            return user
    except Exception as e:
        raise HTTPException(status_code=401,
                            detail="Unauthorized")


