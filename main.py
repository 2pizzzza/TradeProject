from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trading app"
)
# Creating a list of dictionaries for 5 users
users_data = [
    {
        'id': 1,
        'role': 'user',
        'username': 'user1',
        'login': 'user1@example.com',
        'password': 'password1'
    },
    {
        'id': 2,
        'role': 'user',
        'username': 'user2',
        'login': 'user2@example.com',
        'password': 'password2'
    },
    {
        'id': 3,
        'role': 'user',
        'username': 'user3',
        'login': 'user3@example.com',
        'password': 'password3'
    },
    {
        'id': 4,
        'role': 'user',
        'username': 'user4',
        'login': 'user4@example.com',
        'password': 'password4'
    },
    {
        'id': 5,
        'role': 'user',
        'username': 'user5',
        'login': 'user5@example.com',
        'password': 'password5'
    }
]
fake_trades = [
    {
        'id': 1,
        'user_id': 1,
        'currency': 'BTC',
        'side': 'buy',
        'price': 50000.0,
        'amount': 1.0
    },
    {
        'id': 2,
        'user_id': 2,
        'currency': 'ETH',
        'side': 'sell',
        'price': 3000.0,
        'amount': 2.5
    },
    {
        'id': 3,
        'user_id': 3,
        'currency': 'LTC',
        'side': 'buy',
        'price': 150.0,
        'amount': 5.0
    },
    {
        'id': 4,
        'user_id': 4,
        'currency': 'BTC',
        'side': 'sell',
        'price': 52000.0,
        'amount': 0.8
    },
    {
        'id': 5,
        'user_id': 5,
        'currency': 'ETH',
        'side': 'buy',
        'price': 2800.0,
        'amount': 3.0
    }
]


class User(BaseModel):
    id: int
    role: str
    username: str
    login: str
    password: str
    degree: Optional[List['Degree']] = []

class Type_Degree(Enum):
    newbie = "newbie"
    expert = "expert"

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: Type_Degree


@app.get("/users/{user_id}", response_model=List[User])
def hello(user_id: int):
    return [i for i in users_data if i.get("id") == user_id]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=10)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades/")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
