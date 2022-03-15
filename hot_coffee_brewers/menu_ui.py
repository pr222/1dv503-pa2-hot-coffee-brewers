
# List of options for the user
menu_options = {
  1: 'List number of reviews for all Coffee shop',
  2: 'List most liked coffee for all Coffee shop',
  3: 'List the ratings for all coffee to a specific Coffee shop',
  4: 'List most liked coffee for all countries',
  5: 'List the most common roast for all country',
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



