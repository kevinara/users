from fastapi import APIRouter

route = APIRouter()

@route.get("/")
def root():
    return {"message": "Usted se encuentra en la raíz."}