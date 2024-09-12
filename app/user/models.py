import datetime
import uuid

from pydantic import BaseModel, ConfigDict

class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True, frozen=True)

class UserLoginResquest(Base):
    id: str
    pw: str

class UserLoginResponse(Base):
    id: uuid.UUID
    nickname: str
    time_created: datetime.datetime

class Token(BaseModel):
    access_token: str
    token_type: str