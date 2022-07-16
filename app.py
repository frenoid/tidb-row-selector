import mysql.connector
import os
import string
import random
from time import sleep, time


MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_TABLE = os.getenv("MYSQL_TABLE")
QUERY_INTERVAL = os.getenv("QUERY_INTERVAL", "5")


if __name__ == "__main__":
  print("START")
  print(MYSQL_HOST)
  print("READING FROM " + MYSQL_DATABASE + "." + MYSQL_TABLE)
  cnx = mysql.connector.connect(user=MYSQL_USER,
                              password=MYSQL_PASSWORD,
                              host=MYSQL_HOST,
                              port=MYSQL_PORT,
                              database=MYSQL_DATABASE)
  query = "SELECT * FROM " + MYSQL_TABLE

  while True:
    cur = cnx.cursor()
    cur.execute(query)
    for row in cur:
      print(row)
    print("QUERY DONE AT", time())
    print("SLEEPING FOR", QUERY_INTERVAL, "seconds")
    sleep(int(QUERY_INTERVAL))


  cnx.close()
  print("FINISH")
