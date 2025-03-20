from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# URL de conexión a la base de datos
DATABASE_URL = "mssql+pyodbc://DESKTOP-CT3VPT0/GCP?driver=ODBC+Driver+17+for+SQL+Server"

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Proveer una sesión para conectarse
def get_db():
    db = SessionLocal()
    try:
        yield db
        print("Bien")
    finally:
        db.close()
        print("Mal")
