# def createCoffeeTable():
def createCoffeeShopTable():
    return "CREATE TABLE `coffee_shops` (" \
        " `id` VARCHAR(255) NOT NULL," \
        " `name` VARCHAR(255) NOT NULL," \
        " `country` VARCHAR(255) NOT NULL," \
    "  PRIMARY KEY (`id`)" \
        ") ENGINE=InnoDB"


def createReviewsTable():
    return "CREATE TABLE `reviews` (" \
        " `id` INT NOT NULL," \
        " `date` VARCHAR(255) NOT NULL," \
        " `rating` INT NOT NULL," \
        " `coffeeID` INT NOT NULL," \
        " `shopID` VARCHAR(255) NOT NULL," \
    "  PRIMARY KEY (`id`)" \
        ") ENGINE=InnoDB"


def createCoffeeTable():
    return "CREATE TABLE `coffee` (" \
        " `id` INT NOT NULL," \
        " `name` VARCHAR(255) NOT NULL," \
        " `roast` VARCHAR(255) NOT NULL," \
        " `origin` VARCHAR(255) NOT NULL," \
    "  PRIMARY KEY (`id`)" \
        ") ENGINE=InnoDB"

def createReviewTimesView():
    return "CREATE OR REPLACE VIEW reviewtimes AS " \
        "SELECT coffee.name, coffee_shops.country, COUNT(reviews.rating) as ratings " \
        "FROM reviews " \
        "JOIN coffee_shops ON reviews.shopID = coffee_shops.id " \
        "JOIN coffee ON reviews.coffeeID = coffee.id " \
        "GROUP BY coffee_shops.country, coffee.name;" 
