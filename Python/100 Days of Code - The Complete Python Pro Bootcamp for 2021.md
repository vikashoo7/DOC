 Pandas
 -------
 	- CSV sample data for wwather condition "wather_data.csv"
	  Day,Temp,Condition
	  Monday,12,Sunny
	  Tuesday,14,Rain
	  Wednesday,15,Rain
	  Thrusday,14,Cloud
	  Friday,21,Sunny
	  Saturday,22,Sunny
	  Sunday,24,Sunny
	  
 	 - This is the python data analysis library which is helpful in tabular data analysis.
 	 - Panda- Documentation: https://pandas.pydata.org/docs/
         https://pandas.pydata.org/docs/reference/index.html
 	 - The first line of the file is considered as heading.
	 - There are 2 primary data structure of Pandas
	    1. Data Frame (2- dimentional data)
	    2. Series (1- dimentional data)
  
###### Pandas excersise
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
		def add(*arg*):
			for i in args:
				print(i)

		add(1,2,3,4,)

	- "**kwargs" is the way to provide number of keywork argument in the function. Here the passing key word argument is stored in the form of dictionary. 
	  Example:
		def calculate(**kwargs)
			for i in kwargs.items():
			print(i)

		calculate(add=3, multiply=5)
