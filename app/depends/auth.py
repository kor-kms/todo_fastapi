
from fastapi.exceptions import HTTPException


async def current_user(Authorization: Annotated[str|None, Header()]):
    token = Authorization
    user = fake_decode_token(token)
    return user



# header parameter 가져오는 법
# https://fastapi.tiangolo.com/tutorial/header-params/#automatic-conversion

# cookie parameter 가져오는 법
# https://fastapi.tiangolo.com/tutorial/cookie-params/

# @app.get("/users/me")
# async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
#     return current_user


async def is_superuser(user=Depends(current_user)):
    if not user.is_admin:
        raise HTTPException(403)