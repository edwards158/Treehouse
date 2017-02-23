#!/usr/bin/env python
from collections import OrderedDict
import datetime as dt
from  os import system, path, name
import re
from sys import exit

from peewee import *


db = SqliteDatabase('tasklog.db')


class Task(Model):
    employee = CharField(max_length=255)
    name = CharField(max_length=255)
    date = DateField(formats="%Y-%m-%d")
    time = IntegerField(default=0)
    notes = CharField(max_length=255)
    
    class Meta:
        database = db

def initialize():
  """Create the database and the table if they don't exist."""
  db.connect()
  db.create_tables([Task], safe=True)

def clear():
  system('cls' if name == 'nt' else 'clear')


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


def get_task_employee():
  """Get employee name from user"""
  task_employee   = input("Enter the employee name: ")
  if len(task_employee) == 0:
    input("Employee Name should be at least one character long")
    return get_task_employee()
  else:
    return task_employee


def get_task_name():
  """Get name of task from user"""
  task_name   = input("Enter the task name: ")
  if len(task_name) == 0:
    input("Task Name should be at least one character long")
    return get_task_name()
  else:
    return task_name

def convert(date):
    """Converts date to datetime object"""
    conv_date = dt.datetime.strptime(date, 
                    "%Y-%m-%d").date()
    return conv_date
 
def get_task_date(text=""):
  """get the date from the user"""
  task_date = input("Enter date (Format:YYYY-MM-DD): ")
  try:
    dt.datetime.strptime(task_date, "%Y-%m-%d")
  except ValueError:
    input("Please enter date in this format YYYY-MM-DD: Press enter to continue.")
    return get_task_date()
  else:
    return task_date


def get_task_time():
  """Get task time from user"""
  task_time = input("Enter task time in minutes: ")
  try:
    int(task_time)
  except ValueError:
    input("Enter a integer Press enter to continue.")
    return get_task_time()
  else:
    time = int(task_time)
    return time

def get_task_notes():
  """Get the task notes from user"""
  task_notes = input("Enter notes (hit enter to leave empty):")
  return task_notes


def list_entries(entries, search, field):
  """Shows list of search results"""
  clear()
  if entries:
      print("Your search results for {}:\n".format(search))
      for entry in entries:
        if field:
          print(getattr(entry, field))
        else:
          print("Task name: {} \nTask notes: {}".format(entry.name,entry.notes))
      input("Press enter to continue.")
      display_entries(entries)
  else:
      input("No results for {}. Press enter to continue. ".format(search))
      main_menu()


def find_by_date_range():
  """Search file by range of dates. Input start date
  and end date from user """
  print("Enter Start then End date below:")
  start_date = get_task_date("start")
  end_date = get_task_date("end")
  choice = start_date + " - " + end_date

  entries = Task.select().where((Task.date >= start_date) &
                                (Task.date <= end_date))
  
  list_entries(entries, choice, "date")
  return entries


def find_by_employee():
  """get the employeee name from user and search for"""
  data = get_task_employee()
  entries = Task.select().where(Task.employee.contains(data))
  list_entries(entries, data, "employee")
  return entries

    
def find_by_search_term():
  """get the exact input string from user and search"""
  choice = input("Enter term or string: ")
  entries = select_entries()

  entries = entries.where((Task.name.contains(choice)) | 
                           (Task.notes.contains(choice)))
  list_entries(entries,choice,None)
  return entries


def edit_entry(entry):
  """Edit the entries"""
  while True:
    clear()

    print("""
EDIT MENU
---------------------------
What would you like to edit? 
      """)

    print("""
[E] Edit Employee Name
[D] Edit Task Date
[N] Edit Task Name 
[T] Edit Task Time Spent
[S] Edit Task Notes
[M] Main Menu
  """)

    option = input("Please select option from menu: "
          ).lower().strip()

    if option == "e":
      entry.employee = get_task_employee()
      entry.save()
      return(entry)
    if option == "n":
      entry.name = get_task_name()
      entry.save()
      return(entry)
    elif option == "t":
      entry.time = get_task_time()
      entry.save()
      return(entry)
    elif option == "s":
      entry.notes = get_task_notes()
      entry.save()
      return(entry)
    elif option == "d":
      clear()
      entry.date = get_task_date()
      entry.save()
      return(entry)
    elif option == "m":
      main_menu()


def get_entry():
  """Get the entry data from the user"""
  employee = get_task_employee()
  name = get_task_name()
  date = convert(get_task_date())
  
  time = get_task_time()
  notes = get_task_notes()

  entry = {"employee": employee,
    "name": name,
    "date": date,
    "time": time,
    "notes": notes}

  print_entry(entry)

  while True:
    save = input("Would you like to save the entry?"
                  "[y/n]").lower().strip()
    if save == "y":
        input("Entry saved succesfully. Press enter to continue.")
        return entry
    else:
        input("Entry NOT saved.")
        return None


def add_entry():
  """Add an entry"""
  print("""
ADD MENU
---------------------------
    """)
  entry = get_entry()
  if entry:
    return Task.create(**entry)


def delete_entry(entry):
  "Delete and entry from the database"
  
  print("are you sure you wish to delete entry?")
  next_action = input("Action: [Yn]").lower().strip()
  if next_action == "y":
    entry.delete_instance()
    print("Entry deleted!")


def print_entries(index, entries, display=True):
  """Prints the entries from the database"""
  single_entry = entries[index]

  if display:
    print("Displaying {} of {} entry/entries.\n"
      .format(index+1, len(entries)))
  print("Employee: {}".format(single_entry.employee))
  print("Task Name: {}".format(single_entry.name))
  print("Date: {}".format(single_entry.date))
  print("Time Spent (Minutes): {}".format(single_entry.time))
  print("Notes: {}\n".format(single_entry.notes))
  

def display_choices(index, entries):
  """Menu choices to page through multiple entries"""
  p = "[P] - Previous Entry"
  n = "[N] - Next Entry"
  d = "[D] - Delete Entry"
  e = "[E] - Edit Entry"
  m = "[M] - Go back to Main Menu"
  menu = [p, n, d, e, m]

  if index == 0:
    menu.remove(p)
  if index == len(entries) - 1:
    menu.remove(n)
  for menu in menu:
    print(menu)


def select_entries():
    """Retrieves all entries from database"""
    return Task.select().order_by(Task.date.desc())


def display_entries(search=None):
  """Display entries to screen"""

  if search:
    entries = search
  else:
    entries = select_entries()

  res = len(entries)
  if res > 0:
    index = 0
    while True:
      print_entries(index, entries)

      display_choices(index, entries)

      choice = input("\nPlease select option from"
        " menu. ").lower().strip()

      if index == 0 and choice == "n":
        index += 1
        #clear()
      elif (0 < index < len(entries)-1 and choice == "p"):
        index -= 1
        #clear()
      elif (0  < index < len(entries)-1 and choice == "n"):
        index += 1
        #clear()
      elif index == len(entries)-1 and choice == "p":
        index -= 1
        #clear()
      elif choice == 'd':
        return delete_entry(entries[index])  
      elif choice == "e":
        return edit_entry(entries[index])
      elif choice == "m":
        return None
      else:
        print ("Incorrect menu choice\n")

  else:
    input("There are no entries; press enter to continue")


def search_menu():
  """Search for an entry"""
  while True:
    clear()
    print("""
WORKLOG
--------------------------------------------------------
SEARCH MENU
[N] - Find by employee name
[D] - Find by date
[S] - Find by string in task/notes
[M] - Back to main menu
      """)

    option = input("Please select option from menu: "
                ).lower().strip()

    if option in list("ndsm"):
      break
      
  if option == "n":
      search = find_by_employee()
      return search 
  elif option == "d":
      search = find_by_date_range()
      return search
  elif option == "s":
      search = find_by_search_term()
      return search
  elif option == "m":
      main_menu()
  else:
      input("Invalid entry. See menu for valid options. "
          "Press enter to continue.")


def quit_program():
    """Quit and exit program"""
    exit()

menu = OrderedDict([
        ("A", add_entry),
        ("S", search_menu),
        ("V", display_entries),
        ("Q", quit_program)
        ])


def main_menu():
    """Displays main menu"""
    while True:
        clear()
        print("""
WORKLOG MENU
--------------------------------------------------------
MAIN MENU
""")
        for key, value in menu.items():
            print("[{}] - {}".format(key, value.__doc__))

        option = input("\nPlease select option from menu: ").upper().strip()

        if option in menu:
            menu[option]()  
        else:
            input("Invalid choice. Check menu for valid choices.")


if __name__ == "__main__":
  initialize()
  main_menu()