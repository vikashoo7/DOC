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
			

Unlimed Positional Argument
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