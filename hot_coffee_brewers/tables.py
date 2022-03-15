# def createCoffeeTable():
def createCoffeeShopTable():
    return "CREATE TABLE `coffee_shops` (" \
        " `id` VARCHAR(255) NOT NULL," \
        " `name` VARCHAR(255)," \
        " `country` VARCHAR(255)," \
    "  PRIMARY KEY (`id`)" \
        ") ENGINE=InnoDB"


def createReviewsTable():
    return "CREATE TABLE `reviews` (" \
        " `id` INT NOT NULL," \
        " `date` VARCHAR(255)," \
        " `rating` INT," \
        " `coffeeID` INT," \
        " `shopID` VARCHAR(255)," \
    "  PRIMARY KEY (`id`)" \
        ") ENGINE=InnoDB"


def createCoffeeTable():
    return "CREATE TABLE `coffee` (" \
        " `id` INT NOT NULL," \
        " `name` VARCHAR(255)," \
        " `roast` VARCHAR(255)," \
        " `origin` VARCHAR(255)," \
    "  PRIMARY KEY (`id`)" \
        ") ENGINE=InnoDB"
