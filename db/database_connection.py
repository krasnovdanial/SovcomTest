import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2

user = "postgres"
password = "4ty1dmjh1"
host = "localhost"
database = "PersonsData"

DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

try:
    conn = engine.connect()
    print("Успешное подключение к базе данных")
    conn.close()
except Exception as e:
    print("Ошибка подключения:", e)

Base = declarative_base()