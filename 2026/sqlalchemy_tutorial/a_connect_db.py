from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv('DB_URL')

engine = create_engine(DB_URL)

print("Engine created successfully.")

# notes 
"""
    connect() -> return connection objects
    executee() -> execute a sql statement construct
    begin() -> return a context manager delivering a Connnection with a Transaction          established. Upon successful operation, the transaction is committed, else it is rolled back
    dispose() -> dispose of thee connection pool used by the engine
    driver() -> driver name of the Dialect in use by the engine
    table_names() -> return a list of all the table nams available in the database
    transaction() -> executes the given function within a transaction boundary
"""