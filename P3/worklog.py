#!/usr/bin/env python
from csv import DictReader, DictWriter
import datetime as dt
from  os import system, path
import re
from sys import exit

from entry import Entry
import misc as misc
import validator as validator

filename = "worklog.csv"


def clr_screen():
  system('clear')

class Worklog(object):

  def open_file(self, filename):
    """Takes file name as argument and returns a 
    list of dictionary of the entries
    """
    with open(filename, newline="") as csvfile:
      entries = list(DictReader(csvfile, delimiter=","))
    return entries


  def write_entry_to_log(self, entry):
    """write the worklog data to file"""
    file_exists = path.isfile(filename)

    with open (filename, 'a') as csvfile:
      writer = DictWriter(csvfile, delimiter=',', 
      lineterminator='\n',fieldnames=misc.HEADERS)

      if not file_exists:
        writer.writeheader()  # file doesn't exist yet, write a header

      writer.writerow({
        misc.HEADERS[0]: entry.task_name,
        misc.HEADERS[1]: entry.task_time,
        misc.HEADERS[2]: entry.task_date,
        misc.HEADERS[3]: entry.task_notes})


  def list_dates(self,entries):
    """Lists date results and user chooses which entries to view"""
    print("Search gives following results: \n")
    counter = 1
    for entry in entries:
      print("[{}] - {}".format(counter, entry["Date"]))
      counter +=1

  def date_display(self,entries):
      """Look up entry based on list date search results"""
      self.list_dates(entries)
      print("""
    Would you like to:
    [E] - Look up an entry of date on the list
    [S] - Back to Search Menu
    [Q] - Quit and exit the program
    """)
      
      option = input("Please select option from menu: ").lower().strip()

      if option == "e":
        clr_screen()
        self.date_lookup(entries)
      elif option == "s":
        clr_screen()
        self.search_menu()
      elif option == "q":
        self.main_menu()
      else:
        input("Invalid entry. See menu for valid options. "
          "Press enter to continue.")
        clr_screen
        self.date_display(entries)


  def date_lookup(self, entries):
    """Look up entry from result of date search"""
    self.list_dates(entries)
    date = input("\nFrom the list, enter date to look up entry. ")
    
    entry_to_display = []
    
    for entry in entries:
      if date == entry["Date"]:
        entry_to_display.append(entry)
        
    if entry_to_display:
      clr_screen()
      self.display_entries(entry_to_display)   
    else:
      input("Input is not in the search result list. "
        "Try again.")
      clr_screen
      self.date_lookup(entries)


  def search_date_input(self):
    """Validates date entry if in correct format"""

    date_text = validator.check_values(misc.DATE_STRING,
                       validator.validate_date)

    return date_text


  def search_by_range_date(self):
    """Search file by range of dates. Input start date
    and end date from user """
    start = self.search_date_input()
    #print (type(start_date))
    #clr_screen()
    end = self.search_date_input()

    start_date = dt.datetime.strptime(
          start, "%d/%m/%Y")
    end_date = dt.datetime.strptime(
          end, "%d/%m/%Y")

    entries = self.open_file(filename)
    search_result = []

    for entry in entries:
      entry_date = dt.datetime.strptime(entry["Date"], 
            "%d/%m/%Y")
      if start_date <= entry_date and entry_date <= end_date:
        search_result.append(entry)
    
    if search_result:
      clr_screen()
      self.date_display(search_result)
    else:
      print("No result found for date range: {} - {}.".format(
          start, end))
    
    input("Press enter to continue to Search Menu.")

  def display_entry(self,entry):
    """Print the entry before writing to database"""
    print("Task Name: {}".format(entry.task_name))
    print("Time Spent (Mins): {}".format(entry.task_time))
    print("Notes: {}".format(entry.task_notes))
    print("Date: {}\n".format(entry.task_date))
    
  def add_entry(self,entry):
    """Process the entry requirement"""
    self.display_entry(entry)
    print (misc.ADD_MENU)

    for key in sorted(misc.edit_choice_menu):
      print (misc.edit_choice_menu[key])

    choice = input("Please select:")

    if choice == '1':
      self.edit_menu(entry)
      input("Entry edited. Press enter to go back to main menu.")
      clr_screen()
      self.main_menu()
    elif choice == '2':
      self.write_entry_to_log(entry)
      input("Entry written. Press enter to go back to main menu.")
      clr_screen()
      self.main_menu()
    elif choice == '3':
      input("Entry deleted. Press enter to go back to main menu.")
      clr_screen()
      self.main_menu()
    else:
      clr_screen() 
      misc.option_error()
      self.add_entry(entry) 

  def write_del_entry_to_log(self, entry):
    """ write the worklog data to file
    """
    file_exists = path.isfile(filename)

    with open (filename, 'w') as csvfile:
      writer = DictWriter(csvfile, delimiter=',', 
        lineterminator='\n',fieldnames=misc.HEADERS)

      #if not file_exists:
      writer.writeheader()  # file doesn't exist yet, write a header

      for n in entry:
        #print (n['Title'])
        writer.writerow({
          misc.HEADERS[0]: n['Name'],
          misc.HEADERS[1]: n['Time'],
          misc.HEADERS[2]: n['Date'],
          misc.HEADERS[3]: n['Notes']})


  def print_entries(self, index, entries, display=True):
    """Prints the entries in a clean format"""
    if display:
      print("Displaying {} of {} entry/entries.\n"
        .format(index+1, len(entries)))

    print("Task Name: {}".format(entries[index]['Name']))
    print("Time Spent (Minutes): {}"
      .format(entries[index]['Time']))
    print("Date: {}".format(entries[index]['Date']))
    print("Notes: {}\n".format(entries[index]["Notes"]))


  def display_choices(self, index, entries ):
    """Menu choices to page through multiple entries"""
    p = "[P] - Previous Entry"
    n = "[N] - Next Entry"
    m = "[M] - Go back to Main Menu"
    menu = [p,n,m]

    if index == 0:
      menu.remove(p)
    if index == len(entries) - 1:
      menu.remove(n)
    for menu in menu:
      print(menu)

  def display_entries(self, entries):
    """Display entries to screen"""
    index = 0
    
    while True:
      self.print_entries(index, entries)

      if len(entries) == 1:
        input("Press enter to go back to main menu.")
        clr_screen()
        self.main_menu()

      self.display_choices(index, entries)

      choice = input("\nPlease select option from"
        " menu. ").lower().strip()

      if index == 0 and choice == "n":
        index += 1
        clr_screen()
      elif (index > 0 and index < len(entries)-1 
        and choice == "p"):
        index -= 1
        clr_screen()
      elif (index > 0 and index < len(entries)-1 
        and choice == "n"):
        index += 1
        clr_screen()
      elif index == len(entries)-1 and choice == "p":
        index -= 1
        clr_screen()
      elif choice == "m":
        clr_screen()
        self.main_menu()
      else:
        misc.option_error()
        self.main_menu()
        clr_screen()


  def find_by_pattern(self):
    """search the database by pattern"""
    choice = input("Enter pattern to search for:")
    reader = self.open_file(filename)
    pattern = re.compile(".*({}).*".format(choice))
    records = []

    for entry in reader:
      if (re.search(r'{}'.format(choice), entry["Name"]) or
        re.search(r'{}'.format(choice), entry["Notes"])):
        records.append(entry)

    if records:
      self.display_entries(records)
      input("Press enter to continue.")
    else:
      print("No reult found for {} in time spent.".format(choice))

    input("Press enter to continue.")

      
  def find_by_time(self):
    """get the time from user and search"""
    choice = input("Enter time spent to search for:")
    reader = self.open_file(filename)
    records = []

    regex = re.compile(r"\schoice\s") # \s is whitespace


    for entry in reader:
      if re.search(r'{}'.format(choice), entry["Time"]):
        records.append(entry)
    
    if records:
      self.display_entries(records)
      input("Press enter to continue.")
    else:
      print("No reult found for {} in time spent.".format(choice))

    input("Press enter to continue.")

  def find_by_string(self):
    """get the exact input string from user and search"""
    choice = input("Enter exact string to search for:")
 
    reader = self.open_file(filename)
    
    records = []
    for entry in reader:
      if (re.search(r'{}'.format(choice), entry["Name"]) or
        re.search(r'{}'.format(choice), entry["Notes"])):
        records.append(entry)
        
    if records:
      self.display_entries(records)
      input("Press enter to continue.")
    else:
      print("No reult found for {} in time spent.".format(choice))

    input("Press enter to continue.")

  def search_menu(self):
    """Give the user a menu to select what type of search is required"""
    clr_screen() 
    
    print (misc.SEARCH_MENU)

    for key in sorted(misc.search_menu):
      print (misc.search_menu[key])

    print('\n')
    choice = input("Please select:")

    if choice == '1':
      self.search_by_range_date()
      self.main_menu()
    elif choice == '2': 
      self.find_by_time()
      self.main_menu()
    elif choice == '3':
      self.find_by_string()
      self.main_menu()
    elif choice == '4': 
      self.find_by_pattern()
      self.main_menu()
    elif choice == '5': 
      print ("return to main menu")
      self.main_menu()
    else: 
      misc.option_error()
      self.main_menu()

  def main_menu(self):
    """ Give the user a menu to select from"""
    clr_screen()
    print (misc.TITLE_MENU)

    for key in sorted(misc.menu):
      print (misc.menu[key])

    choice = input("Please select from options:")

    if choice == '1':
      print(choice)
      clr_screen() 
      entry = Entry()
      self.add_entry(entry)
    elif choice == '2': 
      self.search_menu()
    elif choice == '3':
      reader = self.open_file(filename)
      self.display_entries(reader)
    elif choice == '4': 
      exit()
    else: 
      misc.option_error()
      self.main_menu()
    

  def __init__(self):
    self.main_menu()

if __name__ == "__main__":
  Worklog()