#!/usr/bin/env python
import datetime as dt
from  os import system, path, name
import re
from sys import exit

from peewee import *

import data_values as values
import misc_dbase as misc

db = SqliteDatabase('tasklog.db')


class Task(Model):
    employee = CharField(max_length=255)
    name = CharField(max_length=255)
    date = DateField(formats="%Y-%m-%d")
    time = IntegerField(default=0)
    date = DateField(formats="%Y-%m-%d")
    notes = CharField(max_length=255)
    
    class Meta:
        database = db


def clear():
  system('cls' if name == 'nt' else 'clear')

def initialize():
  """Create the database and the table if they don't exist."""
  db.connect()
  db.create_tables([Task], safe=True)


def list_entries(entries, search, field):
  """Shows list of search results"""
  clear()
  if entries:
      print("Your search results for {}:\n".format(search))
      for entry in entries:
          print(getattr(entry, field))
      input("Press enter to continue.")
      display_entries(entries)
  else:
      input("No results for {}. Press enter to continue. ".format(search))
      main_menu()

def find_by_date_range():
  """Search file by range of dates. Input start date
  and end date from user """
  
  print("Enter Start then End date below:")
  start = values.get_task_date()
  end = values.get_task_date()
  choice = start + " - " + end

  start_date = dt.datetime.strptime(start, "%Y-%m-%d")
  end_date = dt.datetime.strptime(end, "%Y-%m-%d")

  entries = Task.select().where((Task.date >= start_date) &
                                (Task.date <= end_date))
  list_entries(entries, choice, "date")
  return entries


def find_by_employee():
  """get the employeee name from user and search for"""
  
  data = values.get_task_employee()
  entries = Task.select().where(Task.employee.contains(data))
  list_entries(entries, data, "employee")
  return entries

    
def find_by_search_term():
  """get the exact input string from user and search"""
  data = values.get_task_notes()
  entries = Task.select().where(Task.name.contains(data) | 
                                Task.notes.contains(data))
  display_entries(entries)
  return entries


def edit_entry(entry):
  """Menu to edit the any of the fields in the entry re: 
  name, time, notes and date"""
  print (misc.EDIT_MENU)

  print("""
[1] Edit Employee Name
[2] Edit Task Name 
[3] Edit Task Time Spent
[4] Edit Task Notes
[5] Edit Task Date
  """)

  option = input("Please select option from menu: "
        ).lower().strip()

  if option == "1":
    entry.employee = values.get_task_employee()
    entry.save()
    input("Employee Name edited. Press enter to continue.")
    clear()
    return(entry)
  if option == "2":
    entry.name = values.get_task_name()
    entry.save()
    input("Task Name edited. Press enter to continue.")
    clear()
    return(entry)
  elif option == "3":
    entry.time = values.get_task_time()
    entry.save()
    input("Time Spent edited. Press enter to continue.")
    clear()
    return(entry)
  elif option == "4":
    entry.notes = values.get_task_notes()
    entry.save()
    input("Notes edited. Press enter to continue.")
    clear()
    return(entry)
  elif option == "5":
    clear()
    entry.date = values.get_task_edit_date()
    entry.save()
    input("Date edited. Press enter to continue.")
    clear()
    return(entry)
  else:
    input("Invalid entry. See menu for valid options. "
      "Press enter to continue.")
    clear()
    edit_entry()


def get_entry():
  """Get the entry data from the user"""
  employee = values.get_task_employee()
  name = values.get_task_name()
  date_str = values.get_task_date()
  date = dt.datetime.strptime(date_str,"%Y-%m-%d").date()
  time = values.get_task_time()
  notes = values.get_task_notes()

  entry = {"employee": employee,
    "name": name,
    "date": date,
    "time": time,
    "notes": notes}

  misc.print_entry(entry)

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
  """Process the entry requirement"""
  print (misc.ADD_MENU)
  entry = get_entry()
  if entry:
    return Task.create(**entry)

 
def search_menu():
  """Give the user a menu to select what type of search is required"""
  clear() 
  
  print (misc.SEARCH_MENU)
  print("""
[1] Find by Employee
[2] Find By Date 
[3] Find by Search Term
[4] Return to main menu
  """)

  choice = input("Please select:")

  if choice == '1':
    search = find_by_employee()
    return search
  elif choice == '2': 
    search = find_by_date_range()
    return search
  elif choice == '3':
    search = find_by_search_term()
    return search
  elif choice == '4': 
    print ("return to main menu")
    main_menu()
  else: 
    misc.option_error()
    main_menu()


def delete_entry(entry):
  "Delete and entry from the database"
  
  print("are you sure you wish to delete entry?")
  next_action = input("Action: [Yn]").lower().strip()
  if next_action == 'y':
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
        clear()
      elif (0 < index < len(entries)-1 and choice == "p"):
        index -= 1
        clear()
      elif (0  < index < len(entries)-1 and choice == "n"):
        index += 1
        clear()
      elif index == len(entries)-1 and choice == "p":
        index -= 1
        clear()
      elif choice == 'd':
        return delete_entry(entries[index])  
      elif choice == "e":
        return edit_entry(entries[index])
      elif choice == "m":
        return None
      else:
        misc.option_error()
        main_menu()
        clear()
  else:
    input("No entries found, press any key to continue")


def main_menu():
  """ Give the user a menu to select from"""
  clear()
  print (misc.TITLE_MENU)
  print("""
[1]  Add an Entry
[2]  Search Entries
[3]  Display Entries
[4]  Exit
  """)
  choice = input("Please select from options:")

  if choice == '1':
    clear()
    add_entry()
    main_menu()
  elif choice == '2': 
    search_menu()
    main_menu()
  elif choice == '3':
    display_entries()
    main_menu()
  elif choice == '4':
    exit()
  else: 
    misc.option_error()
    main_menu()

if __name__ == "__main__":
  initialize()
  main_menu()