'''
    List number of reviews for all Coffee Shops.
'''
def query_all_shop_reviews(cursor, cnx):
    query = "SELECT reviews.shopID, coffee_shops.name, COUNT(*)FROM reviews JOIN coffee_shops ON reviews.shopID = coffee_shops.id GROUP BY shopID;"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for result in myresult:
        print(result)


'''
    List all Coffee Shops with their coffee sorts 
    that has an average rating of 4.5 or above.
'''
def query_most_liked_coffee_all_shops(cursor, cnx):
    query2 = "SELECT avgRate.Shop, avgRate.Coffee, avgRate.Rating " \
        "FROM (" \
          "SELECT " \
            "s.name as Shop, " \
            "c.name as Coffee, " \
            "AVG(r.rating) as Rating " \
          "FROM coffee_reviews.reviews r " \
          "JOIN coffee_reviews.coffee c " \
          "ON r.coffeeID=c.id " \
          "JOIN coffee_reviews.coffee_shops s " \
          "ON r.shopID=s.id " \
          "GROUP BY " \
            "s.name, " \
            "c.name " \
        ") avgRate " \
        "WHERE avgRate.Rating >= 4.5 " \
        "GROUP BY avgRate.Shop, avgRate.Coffee;" 
        
    cursor.execute(query2) 
    myresult = cursor.fetchall()
    for result in myresult:
        print(result)

'''
    List average ratings for all different coffees
    for a specific Coffee Shop.
'''
def query_reviews_coffee_specific_shop(input, cursor, cnx):
    query3 = "SELECT coffee.name, AVG(reviews.rating) " \
    "FROM reviews " \
    "JOIN coffee_shops ON reviews.shopID = coffee_shops.id " \
    "JOIN coffee ON reviews.coffeeID = coffee.id " \
    "WHERE coffee_shops.name = '{}' " \
    "GROUP BY coffee.name " \
    "ORDER BY AVG(reviews.rating) DESC;".format(input)

    cursor.execute(query3) 
    myresult = cursor.fetchall()
    for result in myresult:
        print(result)

'''
   Shows the one coffee sort with the most ratings for all countries from the view table
'''
def query_most_rated_coffee(cursor, cnx):
    query4 = "SELECT name, country, ratings " \
    "FROM reviewtimes " \
    "WHERE ratings = (SELECT MAX(ratings) FROM reviewtimes) "

    cursor.execute(query4) 
    myresult = cursor.fetchall()
    for result in myresult:
        print(result)

'''
   Shows the one coffee sort with the least ratings for all countries from the view table
'''
def query_least_rated_coffee(cursor, cnx):
    query5 = "SELECT name, country, ratings " \
      "FROM reviewtimes " \
      "WHERE ratings = (SELECT MIN(ratings) FROM reviewtimes) "

    cursor.execute(query5) 
    myresult = cursor.fetchall()
    for result in myresult:
        print(result)