import os
import pg8000
import sqlite3
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv(dotenv_path="config/db.env")

def connect_db(db_env_var):
    db_url = os.getenv(db_env_var)
    if not db_url:
        raise ValueError(f"Environment variable {db_env_var} not found.")
    
    parsed_url = urlparse(db_url)
    
    if parsed_url.scheme == "postgresql":
        return pg8000.connect(
            host=parsed_url.hostname,
            database=parsed_url.path[1:],
            user=parsed_url.username,
            password=parsed_url.password,
            port=parsed_url.port,
        )
    elif parsed_url.scheme == "sqlite":
        db_path = parsed_url.path.lstrip("/")
        return sqlite3.connect(db_path,check_same_thread=False)
    else:
        raise ValueError(f"Unsupported database type: {parsed_url.scheme}")
    