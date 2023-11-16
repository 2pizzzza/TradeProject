from pydantic import BaseModel
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String),
)

class Operation(BaseModel):
    id = Column(Integer, primary_key=True)
    quantity = Column(String, nullable=False)
    figi = Column(String, nullable=False)
    instrument_type = Column(String, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    type = Column(String, nullable=False)