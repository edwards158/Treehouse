
import datetime as dt
from os import system
import validator as validator

class Entry(object):
  
  def __init__(self):
    self.task_name = ""
    self.task_time = 30
    self.task_notes = ""
    self.task_date = "22/12/1971"
    self.get_task_name()
    self.get_task_time()
    self.get_task_date()
    self.get_task_notes()
    
  def get_task_name(self):
    """Get name of task from user"""
    task_name   = input("Enter the task name: ")
    if len(task_name) == '':
      input("Task Name should be at least one character long. Press enter to continue.")
      self.get_task_name()
    else:
      self.task_name = task_name
      
  def get_task_time(self):
    """Get task time from user"""
    time = input("Enter task time in minutes: ")
    try:
      int(time)
    except ValueError:
      input("Enter a integer Press enter to continue.")
      self.get_task_time()
    else:
      self.time = time

  def get_task_date(self):
    """The time is now"""
    now = dt.datetime.now()
    self.task_date = now.strftime('%d/%m/%Y')
  
  def get_task_edit_date(self):
    """get the date from the user for editing"""
    date = input("Enter date (Format:DD/MM/YYYY): ")
    try:
      dt.datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
      input("Please enter date in this format: DD/MM/YYYY. Press enter to cotinue.")
      self.get_task_edit_date()
    else:
      self.date = date

  def get_task_notes(self):
    """Get the task notes from user"""
    self.task_notes = input("Enter notes (hit enter to leave empty):")
    


