from fastapi import APIRouter, status

from src.adapters.repositories.credentials_unit_of_work \
    import CredentialsUnitOfWork
from src.domain import commands
from src.serivce_layer import messagebus

from src.entrypoints.http.api.v1.req_res_auth_models import (
    TokenResponse,
    UserLoginRequest
)

router = APIRouter()


@router.post(
    '/token',
    status_code=status.HTTP_201_CREATED,
    response_model=TokenResponse
)
async def login(req: UserLoginRequest):
    cmd = commands.UserLoginCommand(
        email=req.email,
        password=req.password)
    uow = CredentialsUnitOfWork()
    token = messagebus.handle(cmd, uow)[0]
    return TokenResponse(token=str(token),
                         token_type='bearer')
