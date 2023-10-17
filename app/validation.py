from typing import Optional
from pydantic import BaseModel, Extra, constr, conint, confloat, EmailStr

# Define the main user data model
class User(BaseModel):
    name: constr(min_length=3, max_length=128)
    age: conint(ge=1, le=120)
    email: EmailStr
    active: Optional[bool]
    score: confloat(ge=0, le=1)

    class Config:
        extra = Extra.forbid

# Define a query model for the user, where all fields are optional
class UserQuery(BaseModel):
    name: Optional[constr(max_length=128)]
    age: Optional[conint(ge=1, le=120)]
    email: Optional[EmailStr]
    active: Optional[bool]
    score: Optional[confloat(ge=0, le=1)]

    class Config:
        extra = Extra.forbid

# Define an update model for the user, where all fields are optional
class UserUpdate(BaseModel):
    name: Optional[constr(max_length=128)]
    age: Optional[conint(ge=1, le=120)]
    email: Optional[EmailStr]
    active: Optional[bool]
    score: Optional[confloat(ge=0, le=1)]

    class Config:
        extra = Extra.forbid

# Sample default instances for each model
default_user = User(
    name="John Smith",
    age=42,
    email="john.smith@gmail.com",
    active=False,
    score=0.5,
)
default_query = UserQuery(
    email="john.smith@gmail.com",
)
default_update = UserUpdate(
    active=True,
    score=0.125,
)