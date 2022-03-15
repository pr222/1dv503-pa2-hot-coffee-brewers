import csv
import mysql.connector
from mysql.connector import errorcode

COFFEE_CSV = ''

def populate_db(CURSOR, CNX):
  print("Parsing to the database...")

  rows = []
  # Read the file.
  with open(COFFEE_CSV, 'r') as file:
    reader = csv.reader(file)
    next(reader) # Skip the first row with column names.
    for row in reader:
      rows.append(row)

  # Remove row if first item/index is not valid. 
  # - A species must have a name.
  for row in rows:
    if row[0] == "NA":
      rows.remove(row)
    elif row[0] == "N/A":
      rows.remove(row)
   
  base_string_species = "INSERT INTO species (" \
                "name, classification, designation, average_height, " \
                "skin_colors, hair_colors, eye_colors, " \
                "average_lifespan, language, homeworld) VALUES ("
                
  end_string_species = ");"
  
  queries = []
  for row in rows:
    query = base_string_species
    for i in row:
      if i == "NA":
        query += "NULL, "
      elif  i == "N/A": 
        query += "NULL, "
      elif i == "indefinite":
        query += "NULL, "
      else:
        hasApostrophe = "'" in i
        if hasApostrophe:
          parts = i.split("'")
          escaped = parts[0] + "\\'" + parts[1]
          query += "'{}', ".format(escaped)
        else:
          query += "'{}', ".format(i)
    # Remove last comma.
    cut = len(query)
    cut = cut - 2
    query = query[0:cut]

    query += end_string_species
    queries.append(query)

  for query in queries:
    try: 
      #print("SQL query {}: ".format(query), end='')
      CURSOR.execute(query)
    except mysql.connector.Error as err:
      print("\n\n******* ERROR! ******* ", err.msg, "\n\n")
    else:
      CNX.commit()
      print("Insert OK.")