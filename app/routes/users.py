from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from datetime import datetime
from app.database import mongodb
from app.models.user import User, UserCreate, PYobjectId

router = APIRouter()

@router.post ('/signup', response_model=User, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate):
    user_dict=user.model_dump()
    user_dict["Created_at"]=datetime.now()
