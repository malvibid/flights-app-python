import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT")),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASS"),
    'database': os.getenv("DB_NAME")
}
