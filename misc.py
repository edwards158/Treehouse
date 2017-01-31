menu = {}
menu['1']="[1] Add Entry." 
menu['2']="[2] Search Entries."
menu['3']="[3] Display Entries"
menu['4']="[4] Exit"


search_menu = {}
search_menu['1']="[1] Find By Date." 
search_menu['2']="[2] Find by Time Spent."
search_menu['3']="[3] Find by Exact Search"
search_menu['4']="[4] Find By Pattern"
search_menu['5']="[5] Return to main menu"
search_menu['6']="[6] Exit the program"

edit_menu = {}
edit_menu['1']="Edit Task Name." 
edit_menu['2']="Edit Task Date"
edit_menu['3']="Edit Task Time"
edit_menu['4']="Edit Task Notes"

edit_choice_menu = {}
edit_choice_menu['1']="[1] Edit the Entry" 
edit_choice_menu['2']="[2] Save the Entry "
edit_choice_menu['3']="[3] Delete the Entry"


MENU_RETURN = "Press enter to return to main menu"
HEADERS = ['Name', 'Time', 'Date', 'Notes']
HEADERS2 = ['  Name', '        Time', 'Date', '        Notes']
DATE_STRING = ("Enter date to display entries in dd/mm/yyyy format:")
TIME_STRING = ("Enter time spent on task:")
STRING_STRING = ("Enter string to search name and notes:")
PATTERN_STRING = ("Enter pattern to search name and notes:")
CHOICE_STRING = ("do you want to return to main menu (y/n)?:")


TITLE_MENU = ("""
WORKLOG MENU
----------------------------
Please enter your choice below: 
      """)

ADD_MENU = ("""
ADD MENU
---------------------------
What would you like to do? 

      """)

EDIT_MENU = ("""
EDIT MENU
---------------------------
What would you like to do? 

      """) 

SEARCH_MENU = ("""
SEARCH MENU
--------------------------- 
      """)

def option_error():
  print ("Unknown Option Selected!")
  input("Press enter to continue.")

