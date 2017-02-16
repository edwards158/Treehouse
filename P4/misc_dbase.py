
def option_error():
  print ("Unknown Option Selected!")
  input("Press enter to continue.")

def print_entry(entry):
    """prints entry to screen"""
    print("""
Employee Name: {employee}
Task Name: {name}
Date: {date}
Time Spent: {time}
Notes: {notes}
""".format(**entry))


MENU_RETURN = "Press enter to return to main menu"
DATE_STRING = ("Enter date to display entries in YYYY-MM-DD format:")
TIME_STRING = ("Enter time spent on task:")

TITLE_MENU = ("""
WORKLOG MENU
----------------------------
Please select from one of the options below: 
      """)

ADD_MENU = ("""
ADD MENU
---------------------------
      """)

EDIT_MENU = ("""
EDIT MENU
---------------------------
What would you like to edit? 
      """) 

SEARCH_MENU = ("""
SEARCH MENU
--------------------------- 
What would you like to search for? 
      """)

DATE_MENU = ("""
DATE MENU
--------------------------- 
 
      """)



