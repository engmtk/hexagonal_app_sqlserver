import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    driver = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    trusted_connection = os.getenv("DB_TRUSTED_CONNECTION", "").lower()

    if not server:
        raise ValueError("Variável DB_SERVER não configurada no .env.")

    if not database:
        raise ValueError("Variável DB_DATABASE não configurada no .env.")

    if trusted_connection == "yes":
        connection_string = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"Trusted_Connection=yes;"
        )
    else:
        username = os.getenv("DB_USERNAME")
        password = os.getenv("DB_PASSWORD")

        if not username:
            raise ValueError("Variável DB_USERNAME não configurada no .env.")

        if not password:
            raise ValueError("Variável DB_PASSWORD não configurada no .env.")

        connection_string = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )

    return pyodbc.connect(connection_string)