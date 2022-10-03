from fastapi import APIRouter

from src.entrypoints.http.api.v1 \
    import authentication_controller, healthcheck


api_router = APIRouter()

api_router.include_router(authentication_controller.router,
                          prefix="/auth",
                          tags=["auth"])

api_router.include_router(healthcheck.router,
                          prefix="/healthcheck",
                          tags=["healthcheck"])
