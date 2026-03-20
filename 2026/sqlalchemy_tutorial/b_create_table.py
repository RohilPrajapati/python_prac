from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from dotenv import load_dotenv
import os

load_dotenv()


DB_URL = os.getenv('DB_URL')

engine = create_engine(DB_URL, echo=True)

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('last_name', String),
)

if __name__ == '__main__':
    meta.create_all(engine)