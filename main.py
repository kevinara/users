from fastapi import FastAPI
from router.routes import route

app = FastAPI()

app.include_router(route)