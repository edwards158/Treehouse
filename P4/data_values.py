import datetime as dt
from os import system
import validator_dbase as validator

def get_task_employee():
  """Get employee name from user"""
  task_employee   = input("Enter the employee name: ")
  if len(task_employee) == '':
    input("Employee Name should be at least one character long. Press enter to continue.")
    get_employee_name()
  else:
    return task_employee

def get_task_name():
  """Get name of task from user"""
  task_name   = input("Enter the task name: ")
  if len(task_name) == '':
    input("Task Name should be at least one character long. Press enter to continue.")
    get_task_name()
  else:
    return task_name
 
def get_task_date():
  """get the date from the user"""
  task_date = input("Enter date (Format:YYYY-MM-DD): ")
  try:
    dt.datetime.strptime(task_date, "%Y-%m-%d")
  except ValueError:
    input("Please enter date in this format YYYY-MM-DD: Press enter to cotinue.")
    get_task_date()
  else:
    return task_date

def get_task_time():
  """Get task time from user"""
  task_time = input("Enter task time in minutes: ")
  try:
    int(task_time)
  except ValueError:
    input("Enter a integer Press enter to continue.")
    get_task_time()
  else:
    return (int(task_time))

def get_task_notes():
  """Get the task notes from user"""
  task_notes = input("Enter notes (hit enter to leave empty):")
  return task_notes
  


