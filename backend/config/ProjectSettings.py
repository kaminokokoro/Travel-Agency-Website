import os
from pathlib import Path

ACCESS_TOKEN_EXPIRE_MINUTES = 3000000
ALGORITHM = "HS256"
def get_root() -> str:
    return str(Path(__file__).parent.parent) + os.sep
private_key = open(get_root()+"private_key.pem", "rb").read()
public_key = open(get_root()+"public_key.pem", "rb").read()