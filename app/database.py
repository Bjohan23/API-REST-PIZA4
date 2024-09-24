from peewee import MySQLDatabase
from config import Config

database = MySQLDatabase(
    Config.MYSQL_DATABASE,
    host=Config.MYSQL_HOST,
    port=Config.MYSQL_PORT,
    user=Config.MYSQL_USER,
    password=Config.MYSQL_PASSWORD
)