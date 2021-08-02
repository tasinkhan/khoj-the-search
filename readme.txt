Project Name:
 ‘Ami Coding Pari Na’

Project Description: 

You have to develop a web application. Your project will contain 3 sections.

Section 1: User Authentication/Registration Page
A user login and registration section. You can use whatever input fields you want (maintaining a standard)

Section 2: Khoj the search Page
After login, users can access this page. 
 Khoj the search: In this segment(page), there will be two input fields
Input Values: User can input comma separated integers
Search Value: User can input only one integer 
Output: Will print True if the search value is in the input values. Otherwise print False

Sample


Now, before showing the output, you have to store the input values in the database in sorted order(descending) along with the logged in user id and the input timestamp. That means, when the user press the button “Khoj”, the Input values (9, 1, 5, 7, 10, 11, 0) will be stored in the database as follows : 11, 10, 9, 7, 5, 1, 0 

So the rough workflow for this section is as follows 

Take the “Input Values”
Take the “Search Value”
Sort the “Input values” in descending order.
Store the sorted “Input Values” in the database.
Check if the “Search Value” is in the “Input Values”
Print the output

In this section, there will be only one API endpoints

Endpoint 1: Get All Input Values

Parameters: start_datetime, end_datetime, user_id

Returns: All the Input Values the user ever entered within start_datetime(inclusive) and end_datetime (inclusive). Check the following response format.

{
    “status”: “succes”,
    “user_id” : 1,
    “payload” : [
         {
              “timestamp” : ”2012-01-01 00:00:00”,
              “input_values” : “11, 10, 9, 7, 5, 1, 0”
          },
         {
                “timestamp” : ”2013-01-01 01:00:00”,
                 “input_values” : “13, 11, 10, 7, 5, 2, 1”
          
       ]
}

Hello!
Hope you are doing well. This is the readme file for project "Ami coding pari na". Hope I can give you all the neccessary informations to run the project. 

*** Make sure you have python installed in your machine***

step 1: Unzip or extract the "Evident_Task" zip file in the Evident_Task folder.
step 2: Browse to the Folder and type cmd in the address bar of the folder then hit 	Enter.
step 3: Type the following lines in cmd one by one.
	"cd env"
	"cd Scripts"
	"activate"
	"cd.."
	"cd.."
	"cd ami_coding_pari_na"
	"py manage.py runserver"

	Hopefully the server will run successfully. then copy the url from the
	terminal and paste in the browser and you can see the project running.
step 4: To accecss the admin panel u will need the superuser id and password.
	url: http://127.0.0.1:8000/admin
	ID: admin
	pass: 123
	
	to create your own superuser close the server using "ctrl c" and type 
	"py manage.py createsuper" in terminal window. provide neccessary 	informations and superuser will be created.

	Thank You.
