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
