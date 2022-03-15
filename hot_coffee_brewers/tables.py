def createCoffeeTable():
    return "CREATE TABLE `coffeeShop` (" \
        " `id` VARCHAR(255) NOT NULL," \
        " `name` VARCHAR(255) NOT NULL," \
        " `country` VARCHAR(255) NOT NULL," \
        "  PRIMARY KEY (`id`) NOT NULL" \
        ") ENGINE=InnoDB"


def createCoffeeShopTable():
    return "CREATE TABLE `review` (" \
        " `id` INT NOT NULL," \
        " `date` VARCHAR(255) NOT NULL," \
        " `rating` INT NOT NULL," \
        " `coffeeName` INT NOT NULL," \
        " `shopId` VARCHAR(255) NOT NULL," \
        "  PRIMARY KEY (`id`) NOT NULL" \
        ") ENGINE=InnoDB"


def createReviewsTable():
    return "CREATE TABLE `coffee` (" \
        " `id` INT NOT NULL," \
        " `name` VARCHAR(255) NOT NULL," \
        " `roast` VARCHAR(255) NOT NULL," \
        " `origin` VARCHART(255) NOT NULL," \
        "  PRIMARY KEY (`id`) NOT NULL" \
        ") ENGINE=InnoDB"
