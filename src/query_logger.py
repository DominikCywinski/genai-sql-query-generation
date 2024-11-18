### Logging queries for privacy purposes ###

import logging

logging.basicConfig(filename="logs/app.log", level=logging.INFO)


def log_query(user_query, sql_query, response):
    logging.info(f"User Query: {user_query}")
    logging.info(f"Generated SQL: {sql_query}")
    logging.info(f"Model Response: {response}")