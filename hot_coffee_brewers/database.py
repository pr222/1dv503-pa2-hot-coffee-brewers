import mysql.connector
from mysql.connector import errorcode
from .tables import *
from .populate_db import *
from .queries import *

# Connection to database
cnx = mysql.connector.connect(user='root', 
                              password='root',
                              unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock')

DB_NAME='coffee_reviews'

cursor = cnx.cursor()

'''
  Add new empty table to the database.
'''
def addTable(table: str):
  try:
    cursor.execute(table)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
      print("Table already exists.")
    else:
      print("ERROR: ", err.msg)
  else:
    print("Table OK.")


'''
  Create a new database
'''
def create_db(cursor, DB_NAME):
  try: 
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
  except mysql.connector.Error as err:
    print("Could not create the database {}".format(err))
    exit(1)
    

'''
  Run database.
'''
def run_db():
  try:
    cursor.execute("USE {};".format(DB_NAME))
    cursor.execute(createReviewTimesView())
  except mysql.connector.Error as err:
    print("The {} database doesn't exist.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Create database...")
      create_db(cursor, DB_NAME)
      print("Database {} was successfully created.".format(DB_NAME))
      cnx.database = DB_NAME

      coffe=createCoffeeTable()
      addTable(coffe)
      
      shop=createCoffeeShopTable()
      addTable(shop)
      
      reviews=createReviewsTable()
      addTable(reviews)

      cursor.execute(createReviewTimesView())

      populate_db(cursor, cnx)
      print("Database tables populated.")
    else:
      print(err)

'''
  Close database connections.
'''
def close_connections():
  # cursor.execute("drop database coffee_reviews")
  cursor.close()
  cnx.close()


'''
  QUERIES
'''
def reviews_all_shops():
  query_all_shop_reviews(cursor, cnx)

def most_liked_coffee_all_shops():
  query_most_liked_coffee_all_shops(cursor, cnx)
  
def reviews_coffee_specific_shop(input):
  query_reviews_coffee_specific_shop(input, cursor, cnx)

def most_rated_coffee():
  query_most_rated_coffee(cursor, cnx)

def least_rated_coffee():
  query_least_rated_coffee(cursor, cnx)