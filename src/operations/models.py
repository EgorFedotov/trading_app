from sqlalchemy import (Integer,
                        String,
                        TIMESTAMP,
                        Table,
                        Column,
                        MetaData,)

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantily", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=False),
    Column("data", TIMESTAMP),
    Column("type", String),
)
