from fastapi import Header, APIRouter
from fastapi.responses import JSONResponse
from tasks import ozon


ozon_router = APIRouter(prefix='/ozon')


def response_error(json_object: dict, status_code: int = 400):
    return JSONResponse(json_object, status_code=status_code)


@ozon_router.get('/actions')
def get_actions(client_id: str = Header(default=None), api_key: str = Header(default=None)):
    if client_id is None:
        return response_error({'message': 'Missing client_id in request headers'})
    if api_key is None:
        return response_error({'message': 'Missing api_key in request headers'})

    ozon.get_actions.delay(client_id, api_key)
    return {'message': 'Task created'}
