from datetime import datetime
from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantily: str
    figi: str
    instrument_type: str
    data: datetime
    type: str
