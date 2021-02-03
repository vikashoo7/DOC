 Randomisation
 -------
 	- Document link: https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
 
 ###### Code Explaination
	- random.randint(1, 10)		##it will generator any number between 1 to 100. 100 is included in the list
	- random.random()			##it will generate the floating number between 0 to 1. 1 is not included.
	- random.random() * 5 		##Generating floating number between between 0 and 5.
List
-------
	- Document link: https://docs.python.org/3/tutorial/datastructures.html
	- It is the collection of many items. 
	- The item can be any data type or mixed data type.
	- The alwasys start the "[" and ends with "]"
	- The index start from "0" and ends with "n-1"
	- Last item of the list can also be denoted as "-1"
	- "append" is use to add the item at the end of the string
		country = ["Linon", "Tiger"]
		country.append("Elephant")
	- "extend" will bunch of the item at the end of the list
		country = ["Linon", "Tiger"]
		country.extend(["Elephant", "Hosrse", "Cat"]
	- List within the list is called Nested List

Function 
-------
	- Documentation Link : https://docs.python.org/3/library/functions.html

	- "def" is used to define a function.
		Syntax:
			def my_function():
				code.

	- function is used to call by its name.
		Syntax:
			my_function()	
	- "return" is the last statment in the function.
	- Docstring
		* it is use to provide the documention of the function. it will describe the function.
		* Docstring can be declealre after first line of the function with in thress quotes.'"""   """"'
		* Syntax:
			def function()
				""" What function does """	### DocStrin

Dictionary
-------
	- This is used to define in the form of key value pair.
	- All the items saparated with ",".
	- Syntax
		key: value
	- Example:
		program_dictionay = {
			"Bug": "An error",
			"Function": "Pice of code",
		}
	- Retrieving items from dictionary
		#print(program_dictionay["Bug"])

	- Adding new items to dictionary
		program_dictionay["loop"] = "Repeting the action"

	- Declearing the empty dictionary
		empty_dictionary = {}

	- Wipe out the existing dictionary
		program_dictionay = {}

	- Editing the new dictionary
		program_dictionay["loop"] = "Repeting the action again"


	- looping through a dictionary
		for key in program_dictionay:
			print(key)				##print key onlt
			print(program_dictionay[key])		##print the value

Nesting list Dictionary
-------

	- Nesting a list and dictionary inside dictionary
		travel_log = {
		  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
		  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
		}

	- Nesting Dictionary inside list
		travel_log = [
		{
		  "country": "France", 
		  "cities_visited": ["Paris", "Lille", "Dijon"], 
		  "total_visits": 12,
		},
		{
		  "country": "Germany",
		  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
		  "total_visits": 5,
		},
		]

class
-------
	- we can create a clas with a clas keyword  follow by clas name.
	- syntax
		calss MyClass:
			paas
	- we can access the clas by creating the object
	- Syntax
		myObject = MyClass()
	- Attribues - are the variable of the class
	- methods are the function of the class.

	- Constructor
		* Also call initialise the object. 
		* we can initialise the constructor with "__init__" function
		* Syntax:
			class myClass:
				def __init__(self):
					##initialise attributes
		* "__init__" function is always called whenever we initialise the object
	
 Pandas
 -------
  
 	 - This is the python data analysis library which is helpful in tabular data analysis.
 	 - Panda- Documentation: https://pandas.pydata.org/docs/
         https://pandas.pydata.org/docs/reference/index.html
 	 - The first line of the file is considered as heading.
	 - There are 2 primary data structure of Pandas
	    1. Data Frame (2- dimentional data)
	    2. Series (1- dimentional data)
  
###### Pandas excersise

 	- CSV sample data for wwather condition "wather_data.csv"
			  Day,Temp,Condition
			  Monday,12,Sunny
			  Tuesday,14,Rain
			  Wednesday,15,Rain
			  Thrusday,14,Cloud
			  Friday,21,Sunny
			  Saturday,22,Sunny
			  Sunday,24,Sunny
	  
	  #data = pandas.read_csv("wather_data.csv")    ##it will read data
	  #print(type(data))                            ###This will print the type of the "data" variable which is "DataFrame"
	  #print(data["Temp"])                          ##it will print Temp colum from the "wather_data.csv"
	  #print(data["Temp"])                          ###This will print the type of the "data" variable which is "Series"
	  #data_dict = data.to_dict()                   ###This will convert the data into the python dictonary
	  #tmp_list = (data["Temp"]).to_list()          ###This will convert the data into the python list
	  #print((data["Temp"]).mean())			###This will print the average of the list
	  #print((data["Temp"]).max())			###This will print the highest value in the series data
	  #print(data.Temp)				###This is the other way to print the series (cloumn)
	  #print(data[data.Day == "Monday"])		###Print the entire row where the value of "Day=Monday"
	  #print(data[data.Temp == data.Temp.max()])	###Print the entire row where the temp is maximum.
	  #moday = data[data.Day == "Monday"] ; monday_temp_f = int(moday.Temp)*9/5*32		###Convert the temperature celsius to fahrenheit from the "wather_data.csv"

	  * Creating the data frame from the scracth
  	data_dict = {
		"student" : ["Amy", "James", "Angela"],
		"scores" : [76, 56, 65]
		}
	#new_data=pandas.DataFrame(data_dict)		###Create the new Data Frame from dictonary
	#new_data.to_csv("new_data")			###Create the new csv file with "new_data" name
 


How to Create Lists using List Comprehension
------------------------------------
	 *  list Comprehension - its a case where we create a new list from the previous list.
	syntax:
		new_list = [new_item for item in old_list]
	Example:
		list = [1, 2, 3]
		new_list = [ item+1 for item in list ]

	* conditional list Comprehension
	syntax:
		new_list = [new_item for item in old_list if condition]
	Example:
		list = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
		short_name = [ name for name in list if len(name) < 5]

	* Dictionary Comprehension
	syntax:
		new_dict ={new_key:new_value for item in list}
		new_dict ={new_key:new_value for (key, value) in dict.items if condition}
	Example:
		list = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
		import random
		student_score = {student:random.randint(1, 100) for student in name}		##creating dictionary from the list
		passed_student = {student:score for (student, score) in student_score.items() if score > 60 }	##create the dictionary.. the student whose score more than 60
		
	* itterating Pandas DataFram
			import pandas
			student_dict = {
				student": ["Angela", "James", "Lily"]
				"score": [56,76,98]
			}
			student_data_frame = pandas.DataFrame(student_dict)
			for (index, row) in student_data_frame.iterrows():
				print(index)		##this will print panda index
				print(row)		##this will print panda row. each row is the data series.
		
TKinter
-------
	it is used to create graphical user interface (GUI).
	it come with python installation by default.
	Documentation link = "https://docs.python.org/3/library/tkinter.html"
	
###### Code Explaination
	- window = tkinter.Tk()	##Initialising the object. TK is the class in the tkinter. Ini
	- window.title("My First GUI Program")	##Change the title of the GUI	
	- window.minsize(width=500, height=300)
	- window.config(padx=10, pady=10)	##leave the margin in the layout
	- my_label = tkinter.Label(text="I Am a Label", font=("Ariel", 24,"bold"))	##create the label
	  my_label.pack()		##Print the label
	- window.mainloop()	##keep the window open. this will be the end of the program
	- button = tkinter.Button(text="click Me")	##Create the button
	  button.pack()					##display the button
	- Adding the function in the button
		def button_clicked():
			print("I got clicked")
			my_label.config(text="Button Got Clicket")	##This will change the existing label after click
			
		button = tkinter.Button(text="click Me", command=button_clicked)
		button.pack()
	- input = tkinter.Entry(width=10)		##create the input box in the screen
	- imput.pack()				##display the input box
	  input.get()				##print the input in the input box as a string

###### Layout Manager
	pack - it is the layout Manager.it starts running from the top to bottom. It will pack all the wedget one by one. The limitation is the pack is that it is very difficult to posting the wedget to the required place.
	Syntax:
		my_label.pack()

	place - it is the layout Manager. It is all about the presise positioning. The limitation of the of the place that it is very difficult to manage if the wedget is large in number.
	Syntax:	
		my_label.place(x=100, y=200)

	Grid - it is the layout Manager. The whole layout is divided into row and cloumn. wedget will allign based on the row and cloumn.
	Syntax
		my_label.grid(column=1, row=4)

	Note: we cannot mix up grid and pack in the same program.

###### Sample code for basic Tkinter component

	from tkinter import *

	#Creating a new window and configurations
	window = Tk()
	window.title("Widget Examples")
	window.minsize(width=500, height=500)

	#Labels
	label = Label(text="This is old text")
	label.config(text="This is new text")
	label.pack()

	#Buttons
	def action():
	    print("Do something")

	#calls action() when pressed
	button = Button(text="Click Me", command=action)
	button.pack()

	#Entries
	entry = Entry(width=30)
	#Add some text to begin with
	entry.insert(END, string="Some text to begin with.")
	#Gets text in entry
	print(entry.get())
	entry.pack()

	#Text
	text = Text(height=5, width=30)
	#Puts cursor in textbox.
	text.focus()
	#Adds some text to begin with.
	text.insert(END, "Example of multi-line text entry.")
	#Get's current value in textbox at line 1, character 0
	print(text.get("1.0", END))
	text.pack()

	#Spinbox
	def spinbox_used():
	    #gets the current value in spinbox.
	    print(spinbox.get())
	spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
	spinbox.pack()

	#Scale
	#Called with current scale value.
	def scale_used(value):
	    print(value)
	scale = Scale(from_=0, to=100, command=scale_used)
	scale.pack()

	#Checkbutton
	def checkbutton_used():
	    #Prints 1 if On button checked, otherwise 0.
	    print(checked_state.get())
	#variable to hold on to checked state, 0 is off, 1 is on.
	checked_state = IntVar()
	checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
	checked_state.get()
	checkbutton.pack()

	#Radiobutton
	def radio_used():
	    print(radio_state.get())
	#Variable to hold on to which radio button value is checked.
	radio_state = IntVar()
	radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
	radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
	radiobutton1.pack()
	radiobutton2.pack()


	#Listbox
	def listbox_used(event):
	    # Gets current selection from listbox
	    print(listbox.get(listbox.curselection()))

	listbox = Listbox(height=4)
	fruits = ["Apple", "Pear", "Orange", "Banana"]
	for item in fruits:
	    listbox.insert(fruits.index(item), item)
	listbox.bind("<<ListboxSelect>>", listbox_used)
	listbox.pack()
	window.mainloop()			

Unlimited Positional Argument
----------
	- "*arg" is the way to provide n number of the argument in the function. here the passing argument is stored in the form of touple.
	  Example:
		def add(*arg):
			for i in args:
				print(i)

		add(1,2,3,4,)

	- "**kwargs" is the way to provide number of keywork argument in the function. Here the passing key word argument is stored in the form of dictionary. 
	  Example:
		def calculate(**kwargs)
			for i in kwargs.items():
			print(i)

		calculate(add=3, multiply=5)

Handling Errors and Exception
-------

	-Types of error
		* FileNotFound - happen when file path not present.
		* KeyError - happen when access the element which not present in the dictionary
		* IndexError - happen when access the element which not present in the list
		* TypeError - happend when we add string and integer

	- To avoid the errors, we will use error handling.
	- Syntax:
		try:
			code for set of task
		except:
			Do this if there was an exception
		else:
			this will run if there was no exception
		finally:
			This will run every time

	- There can be multiple except block
	- Example:
		try:
			file = open("myfile.txt")
			a_dictionary - {"key":"value}
			print(a_dictionary["other_key"]
		except FileNotFoundError:
			file = open"(myfile.txt","w")
			file.write("write some thing")
		except KeyError as error_message:
			print(f"The key {error_message} does not exists.")

		else:
			content = file.read()
			print(content)
		finally:
			file.close()
			print("File was closed")

	- Raising the own Exception
		* "raise" keyword is used to create the exception
		* Primarily this is the way to create error.
		* example:
			##we are calulating BMI
			height = float(input("Height: "))
			weight = float(input("Weight: "))

			if height > 3:
				raise ValueError ("Human Height should not be more than 3 Meter")		##creating the error. Human height more that 3 M is unrealistic. So error need to notify.

			bmi = weight / height
			print(bmi)

datetime module
-------
	- it is comming with pre-loaded with python.
	- Example
		now = datetime.datetime.now()	##proide the latset time
		year = now.year		##provide the year


	- Providing the custome data
		data_of_birth = datetime.datetime(year=2020, month=12, day=15, hour=4)


API (Application Programming Interface)
----
	- It is a set of commands, function, protocols, and object that program can use to interact with an external system.
	- The API return the data in json formate.
	- "request" module is use to call the API
	- Documentation : http://open-notify.org/Open-Notify-API/ISS-Location-Now/
	- Status Code URL: https://httpstatuses.com/
	- Request Module URL: https://pypi.org/project/requests/
	- Response Code sumarry
		* 1XX : wait
		* 2XX : working
		* 3XX : No permission
		* 4XX : thing we looking for does not exists
		* 5XX : server has issue
		
	- Example:
		import request
		response = request.get(url="http://api.open-notify.org/iss-now.json")		##this will get the data
		print(respose)							##this will print the response code. 200 -> means request is successful else request is unsuccessful.
		response.raise_for_status()		##This will print the error code except 200
		data = response.json()			##print the all the data
		longitude = data["iss_position"]["longitude"]	##print the specific data from the data variable
		latitude = data["iss_position"]["latitude"]
		iss_position(longitude, latitud)
		print(iss_position)







	######API Parameter
	- response = request.get(URL, parama=parameter)
	- https://api.sunrise-sunset.org/json?lat=1.23456&lng=-1.345	##passing the parameter via url
	- Example
		MY_LAT = 1.23456
		My_LONG = -1.345

		parameters = {
			"lat" = MY_LAT
			"lng" = My_LONG
		}

	response = request.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()
	data = response.json()
	print(data)
