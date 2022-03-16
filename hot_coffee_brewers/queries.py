

'''
    List number of reviews for all Coffee Shops.
'''
def query_all_shop_reviews(cursor, cnx):
    query = "SELECT reviews.shopID, coffee_shops.name, COUNT(*)FROM reviews JOIN coffee_shops ON reviews.shopID = coffee_shops.id GROUP BY shopID"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for result in myresult:
        print(result)
        
'''

'''
def query_most_liked_coffee_all_shops(cursor, cnx):
    query = "SELECT reviews.shopID, coffee_shops.name, COUNT(*)FROM reviews JOIN coffee_shops ON reviews.shopID = coffee_shops.id GROUP BY shopID"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for result in myresult:
        print(result)