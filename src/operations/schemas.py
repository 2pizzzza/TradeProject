from fastapi_users import schemas


class OperationRead(schemas.SCHEMA):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    type: int
    amit: int
class OperationCreate(schemas.SCHEMA):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    type: str