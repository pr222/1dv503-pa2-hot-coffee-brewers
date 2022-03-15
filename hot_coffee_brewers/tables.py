def createCoffeeTable():
  return "CREATE TABLE `species` (" \
                      " `name` VARCHAR(255) NOT NULL," \
                      " `classification` VARCHAR(255)," \
                      " `designation` VARCHAR(255)," \
                      " `average_height` INT," \
                      " `skin_colors` VARCHAR(255)," \
                      " `hair_colors` VARCHAR(255)," \
                      " `eye_colors` VARCHAR(255)," \
                      " `average_lifespan` INT," \
                      " `language` VARCHAR(255)," \
                      " `homeworld` VARCHAR(255)" \
                      ") ENGINE=InnoDB" 