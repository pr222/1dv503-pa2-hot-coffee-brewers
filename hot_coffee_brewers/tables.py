def createCoffeeTable():
  return "CREATE TABLE `coffeeShop` (" \
                      " `id` VARCHAR(255) NOT NULL," \
                      " `name` VARCHAR(255)," \
                      " `country` VARCHAR(255)," \
                      ") ENGINE=InnoDB" 
                      
def createCoffeeShopTable():
  return "CREATE TABLE `review` (" \
                      " `id` INT NOT NULL," \
                      " `date` VARCHAR(255)," \
                      " `rating` INT," \
                      " `coffeeName` INT," \
                      " `shopId` VARCHAR(255)," \
                      ") ENGINE=InnoDB" 
                      
def createReviewsTable():
  return "CREATE TABLE `coffee` (" \
                      " `id` INT NOT NULL," \
                      " `name` VARCHAR(255)," \
                      " `roast` VARCHAR(255)," \
                      " `origin` VARCHART(255)," \
                      ") ENGINE=InnoDB" 