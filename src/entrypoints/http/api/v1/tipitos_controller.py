from fastapi import APIRouter, status

from src.adapters.repositories.tipito_unit_of_work import TipitoUnitOfWork
from src.domain import commands
from src.serivce_layer import messagebus

from src.entrypoints.http.api.v1.req_res_tipitos_models import (
    TipitoResponse,
    TipitoCreateRequest
)

router = APIRouter()


@router.get(
    '/{name}',
    status_code=status.HTTP_200_OK,
    response_model=TipitoResponse
)
async def get_tipito(name: str):
    cmd = commands.TipitoCreateCommand(
        name=name
    )
    uow = TipitoUnitOfWork()
    tipito = messagebus.handle(cmd, uow)[0]
    return TipitoResponse(name=tipito.name)


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=TipitoResponse
)
async def create_tipito(req: TipitoCreateRequest):
    cmd = commands.TipitoCreateCommand(
        name=req.name)
    uow = TipitoUnitOfWork()
    tipito = messagebus.handle(cmd, uow)[0]
    return TipitoResponse(name=tipito.name)
