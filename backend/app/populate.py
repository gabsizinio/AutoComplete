import json
import asyncio
from .db import database
from .models import suggestions

async def populate():
    await database.connect()

    with open("Scraper/glossario_cnmp.json", "r", encoding="utf-8") as f:
        termos = json.load(f)

    valores = [{"text": termo} for termo in termos]
    await database.execute_many(suggestions.insert(), valores)

    await database.disconnect()

if __name__ == "__main__":
    asyncio.run(populate())
