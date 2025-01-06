from pydantic import BaseModel, ConfigDict

class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True, frozen=True)

class UserLoginResquest(Base):
    id: str
    pw: str

class UserLoginResponse(Base):
    token: str
    nickname: str
