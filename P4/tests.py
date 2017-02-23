import unittest
import unittest.mock as mock

import worklog_dbase


from peewee import *
from playhouse.test_utils import test_database

test_db = SqliteDatabase(':memory:')
test_db.connect()
test_db.create_tables([worklog_dbase.Task], safe=True)

TEST = {"employee": "jon james",
         "name": "maths",
         "date": "2010-01-01",
         "time": 55,
         "notes": "walking the dog"
         }


class AddTests(unittest.TestCase):

  @staticmethod
  def create_entries():
      worklog_dbase.Task.create(
          employee=TEST["employee"],
          name=TEST["name"],
          date=TEST["date"],
          time=TEST["time"],
          notes=TEST["notes"])


  def test_get_task_employee(self):
    with mock.patch('builtins.input', return_value=
        TEST["employee"]):
        assert worklog_dbase.get_task_employee() == TEST["employee"]
    
    with mock.patch('builtins.input', side_effect = ["", "", 
        "jon"]):
        self.assertEqual(worklog_dbase.get_task_employee(),"jon")


  def test_get_task_time(self):
    with mock.patch('builtins.input', side_effect = ["one", 
        "", 6]):
        self.assertEqual(worklog_dbase.get_task_time(),6)


  def test_get_task_name(self):
    with mock.patch('builtins.input', side_effect = ["", 
        "", "studying"]):
        self.assertEqual(worklog_dbase.get_task_name(),"studying")


  def test_get_task_date(self):
    with mock.patch('builtins.input', side_effect = ["05/05/2016", 
        "", "2016-05-05"]):
        self.assertEqual(worklog_dbase.get_task_date(),"2016-05-05")


  def test_add_entry(self): 
    with mock.patch('builtins.input', side_effect = ["test name",
        "eating", "2016-11-06", 50, "fgf f", "tt", ""], return_value=
        TEST):
        assert worklog_dbase.add_entry()==None

  def test_search_menu(self):
    with test_database(test_db, (worklog_dbase.Task, )):
        self.create_entries()

        
        with mock.patch('builtins.input', side_effect = 
        ["n", "jon james", "", "m"]):
          assert worklog_dbase.search_menu().count() == 1

                        
        with mock.patch('builtins.input', side_effect = 
        ["s", "maths", "", "m"]):
            assert worklog_dbase.search_menu().count() == 1           

        with mock.patch('builtins.input', side_effect = 
        ["s", "walking", "", "m"]):
            assert worklog_dbase.search_menu().count() == 1           
        
        
  def test_edit_entry(self):
    with test_database(test_db, (worklog_dbase.Task, )):
      entry = worklog_dbase.Task.create(**TEST)
        
      with mock.patch('builtins.input', side_effect = 
      ["s","coding", ""]):
          worklog_dbase.edit_entry(entry)
          self.assertEqual(entry.notes, "coding")
      
      with mock.patch('builtins.input', side_effect = 
      ["e","marley", ""]):
          worklog_dbase.edit_entry(entry)
          self.assertEqual(entry.employee, "marley")

      with mock.patch('builtins.input', side_effect = 
      ["d","2000-01-01", ""]):
          worklog_dbase.edit_entry(entry)
          self.assertEqual(entry.date, "2000-01-01")

      with mock.patch('builtins.input', side_effect = 
      ["t", 500, ""]):
          worklog_dbase.edit_entry(entry)
          self.assertEqual(entry.time, 500)              

      with mock.patch('builtins.input', side_effect = 
      ["n","techdegree", ""]):
          worklog_dbase.edit_entry(entry)
          self.assertEqual(entry.name, "techdegree") 


  def test_delete_entry(self):
    with test_database(test_db, (worklog_dbase.Task, )):
      entry = worklog_dbase.Task.create(**TEST)        
      with unittest.mock.patch('builtins.input', side_effect = 
      ["y"]):
          worklog_dbase.delete_entry(entry)
          self.assertEqual(worklog_dbase.Task.select().count(), 0)
            

if __name__ == "__main__":
    unittest.main()