from app.models import suggestions
from app.db import engine, metadata

if __name__ == "__main__":
    metadata.create_all(engine)
    print("Tabelas criadas com sucesso!")
