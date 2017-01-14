import datetime as dt

def validate_date(date_text):
	try:
	  dt.datetime.strptime(date_text, '%d/%m/%Y')
	except ValueError:
	  raise ValueError("Incorrect data format should be dd/mm/yyyy")

def validate_time(time_text):
	try:
	  val = int(time_text)
	except ValueError:
	  raise ValueError("That is not an integer")

def validate_string(string_text):
	
	val = (string_text)
	if val == '':	
		raise ValueError("That is a empty string")
	  
def check_values(message_string,function_name):
  
  entry = False
  while not entry:
      try:
        data_text = input(message_string)
        function_name(data_text)
      except ValueError as ve:
        print(ve)
        continue
      entry = True
  return data_text


def validate_menu_choice(menu_string):
		
	if menu_string.lower() not in ['y','n']:
		raise ValueError('enter y or n')


def validate_row_exists(menu_choice,num_rows):
		
	if menu_choice not in range(0,num_rows):
		raise ValueError('enter y or n')





 