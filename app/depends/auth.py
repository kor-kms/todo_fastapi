
from typing import Union
from datetime import datetime

from app.errors.excpetion import ForbiddenException
from fastapi import Header
from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

async def get_current_user(token: Union[str, None] = Header(default=None)):
    try:
        decrypted_token = cipher_suite.decrypt(token)
    except:
        raise ForbiddenException

    user_id = decrypted_token.decode('utf-8').split('-')[0]
    return int(user_id)


async def get_token(id: str):
    token = bytes(f"{id}-Simple-token-{datetime.now()}", 'utf-8')
    cipher_token = cipher_suite.encrypt(token)
    return cipher_token