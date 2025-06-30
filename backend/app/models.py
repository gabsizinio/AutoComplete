from sqlalchemy import Table, Column, Integer, String
from app.db import metadata

suggestions = Table(
    "suggestions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String, index=True),
)
