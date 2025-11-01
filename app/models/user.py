from pydantic import BaseModel,EmailStr
from typing import Optional
from  datetime import datetime
from bson import ObjectId

# Create a custom type that handles MongoDB ObjectID conversion from API/JSON to ObjectId in MonogoDb and back
class PYobjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v): #Checks if the input is a valid objectId
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema): # tells OpenApi that these field is to be treated as API documentation
        field_schema.update(type="string")

class UserBase(BaseModel):
    name:str
    email:EmailStr
    age:Optional[int] =None
    password:str
class UserCreate(UserBase):
    pass
class User(UserBase):
    id:PYobjectId #Uses our custom ObjectID handler
    created_at:datetime

    class Config:
        arbitrary_types_allowed = True #Allows non-pydantic types like ObjectId
        json_encoders = {ObjectId: str} #Converts ObjectId to string in Json
