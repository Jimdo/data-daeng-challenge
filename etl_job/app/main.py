# Implement your ETL Pipeline here
import json

import psycopg2
import requests


def get_connection():
    return psycopg2.connect(
        dbname="dwh", user="postgres", password="postgres", host="localhost", port=5432
    )


def ddl(cur) -> None:
    cur.execute("create schema if not exists dash")
    cur.execute(
        """
        create table if not exists dash.statistics (
        )
    """
    )


if __name__ == "__main__":
    # TODO
    print("Hello")
