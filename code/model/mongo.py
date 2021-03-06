# -*- coding: utf-8 -*-

try:
  from urllib.parse import quote_plus
except ImportError:
  from urllib import quote_plus

from bson import ObjectId
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from typing import Text, NoReturn, Callable
from variables.general import logger

class Mongo():

  def __init__(self, host: Text,
                user: Text,
                password: Text,
                port=27017) -> NoReturn:
    self.uri = f"mongodb://{quote_plus(user)}:{quote_plus(password)}@{host}:{port}"

  def get_connection(self) -> MongoClient:
    try:
      conn = MongoClient(self.uri, serverSelectionTimeoutMS=1)
      conn.server_info()
      try:
        conn.admin.command("ismaster")
      except ConnectionFailure:
        logger.error(f"Could not connect to MongoDB: {error}")
      finally:
        try:
          conn["admin"].command("serverStatus")
        except Exception as error:
          logger.error(f"General Exception Mongo - {error}")
        else:
          logger.info("You are connected!")
        return conn
    except ServerSelectionTimeoutError  as error:
      logger.error(f"Server Timeout Error - {error}")

  def close_connection(self, client: Callable) -> NoReturn:
    logger.info("Connection getting closed")
    client.close()

  def list_databases(self) -> NoReturn:
    for index, value in enumerate(self.client.list_database_names(), start=1):
      logger.info(f"Database {index} - {value}")

  def show_status(self) -> NoReturn:
    print(self.client["admin"].command("serverStatus"))
