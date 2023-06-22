from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import enum

app = FastAPI(
    title="Trading App"
)

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )

fake_users = [
    {'id': 1, 'role': 'admin', 'name': ['Egor']},
    {'id': 2, 'role': 'investor', 'name': 'Petr'},
    {'id': 3, 'role': 'trader', 'name': 'Nikita'},
    {'id': 4, 'role': 'investor', 'name': 'Tatarin', 'degree': [
        {'id': 1, 'created_at': '2023-01-01T00:00:00', 'type_degree': 'expert'}
    ]},
]


class DegreeType(enum.Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.15,},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.15,},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}

