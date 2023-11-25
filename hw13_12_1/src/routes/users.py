# src\routes\users.py
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session


from src.database.conn_db import get_db
from src.database.models import User

# from src.services.auth import get_current_user
# import cloudinary
# from cloudinary.uploader import upload

from src.schemas import  UserResponse, UserDb
from src.services.cloudinary import Cloudinary

# from src.config import settings

from src.services.auth import auth_service
router = APIRouter(prefix="/users", tags=["users"])




# @router.get("/me/", response_model=UserResponse, response_model_exclude_none=True)
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user

@router.get("/me", response_model=UserDb)
async def read_me(current_user: User = Depends(auth_service.get_current_user)):
    user_db = UserDb(**current_user.__dict__.copy())
    return user_db



@router.patch("/avatar", response_model=UserResponse, 
              response_model_exclude_unset=True)
async def update_avatar_user(
    file: UploadFile = File(), 
    current_user: User = Depends(auth_service.get_current_user), 
    db: Session = Depends(get_db)
):
    public_id = Cloudinary.generate_public_id_by_email(str(current_user.email))
    r = Cloudinary.upload(file.file, public_id)

    src_url = Cloudinary.generate_url(r, public_id)
    user_db = UserDb(**current_user.__dict__.copy())
    user = await auth_service.update_avatar(current_user.email, src_url, db)
    return UserResponse(user=user_db)