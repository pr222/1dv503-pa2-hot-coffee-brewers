
# List of options for the user
menu_options = {
  1: 'List all planets',
  2: 'Search for planet details',
  3: 'Search for species with height higher than given number',
  4: 'What is the most likely desired climate of the given species?',
  5: 'What is the average lifespan per species classification?',
  6: 'Exit',
}

# Prints the user menu options
def print_menu():
  # Menu code inspired from https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
  for key in menu_options.keys():
      print(key, '--', menu_options[key])

      
      # Calls method from users input option
if __name__ == '__main__':
  while(True):
      print_menu()
      option = ''
      try:
          option = int(input('Enter your choice: '))
      except:
          print('Wrong input. Please enter a number ...')
      # if option == 1:
      #     listPlanets()
      # elif option == 2:
      #     planetDetails()
      # elif option == 3:
      #     speciesHeight()
      # elif option == 4:
      #     climateForSpecies()
      # elif option == 5:
      #     speciesLifespan()
      # elif option == 6:
      #     print('Exit application')
      #     exit()
      # else:
      #     print('Invalid option. Please enter a number between 1 and 6.')



