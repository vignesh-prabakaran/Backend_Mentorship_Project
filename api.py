from fastapi import APIRouter

from routes import auth, user

router = APIRouter(prefix="/api")

router.include_router(auth.router)

router.include_router(user.router)