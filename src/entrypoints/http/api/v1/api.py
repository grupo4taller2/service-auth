from fastapi import APIRouter

from src.entrypoints.http.api.v1 import tipitos_controller, healthcheck


api_router = APIRouter()

api_router.include_router(tipitos_controller.router,
                          prefix="/tipitos",
                          tags=["tipitos"])

api_router.include_router(healthcheck.router,
                          prefix="/healthcheck",
                          tags=["healthcheck"])
