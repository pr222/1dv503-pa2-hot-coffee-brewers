from pydoc import importfile
from .database import run_db, close_connections
from .menu_ui import print_menu

print("Im feeling hot hot hot")

run_db()
print_menu()
close_connections()