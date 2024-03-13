from fastapi import FastAPI

from router.auth import router as auth_router
from router.users import router as users_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
