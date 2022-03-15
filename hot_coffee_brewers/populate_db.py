import csv
import mysql.connector
from mysql.connector import errorcode

COFFEE_CSV = './data/coffee.csv'
SHOPS_CSV = './data/coffeeShop.csv'
REVIEWS_CSV = './data/reviews.csv'

def populate_db(cursor, cnx):
  '''
    COFFEE TABLE
  '''
  with open(COFFEE_CSV, 'r') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    # Skip column names
    next(csvfile, None)
    for row in csvfile:
      # Check columns
      for i in range(len(row)):
          if row[i] == 'NA':
            row[i] = None
      # if name is NA        
      if row[0] == None:
          continue
      query = "INSERT INTO `coffee`(id,name,roast,origin)VALUES(%s,%s,%s,%s);"
      cursor.execute(query, row)
    cnx.commit()
    
  '''
    REVIEWS TABLE
  '''
  with open(REVIEWS_CSV, 'r') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    # Skip column names
    next(csvfile, None)
    for row in csvfile:
      # Check columns
      for i in range(len(row)):
          if row[i] == 'NA':
            row[i] = None
      # if name is NA        
      if row[0] == None:
          continue
      query = "INSERT INTO `reviews`(id,date,rating,coffeeID,shopID)VALUES(%s,%s,%s,%s,%s);"
      cursor.execute(query, row)
    cnx.commit()   
     
  '''
    COFFEE SHOPS TABLE
  '''
  with open(SHOPS_CSV, 'r') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    # Skip column names
    next(csvfile, None)
    for row in csvfile:
      # Check columns
      for i in range(len(row)):
          if row[i] == 'NA':
            row[i] = None
      # if name is NA        
      if row[0] == None:
          continue
      query = "INSERT INTO `coffee_shops`(id,name,country)VALUES(%s,%s,%s);"
      cursor.execute(query, row)
    cnx.commit()
