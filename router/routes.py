from fastapi import APIRouter
from schema.user_schema import UserSchema

route = APIRouter()

@route.get("/")
def root():
    return {"message": "Usted se encuentra en la raíz."}

@route.post("/api/user")
def create_user(user_data:UserSchema):
    print(user_data)