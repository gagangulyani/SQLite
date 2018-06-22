import sqlite3
import os,os.path
import base64

print ("""
=====================================================================
			Simple SQLite Example
	     		 by (Doesn't really matter)
=====================================================================
""")


db_name='Dummy_DB.db'  #The Dummy Database

file=sqlite3.connect(db_name)  # Opening (and connecting) the DB file

cursor=file.cursor()   #Creating DB cursor file

try:                               #Creating Users Table for Saving username and password
	#The Ultimate SQL create table querry
	cursor.execute("""                      
	create table IF NOT EXISTS Users(
	id integer primary key AUTOINCREMENT,
	username text,
	password text)""")


except Exception as e:             # If any error occurs..program terminates..
	print (e)
	exit()

user_inf={}              # Dictionary for storing user info

while True:
	print ("\nEnter 1 to insert user info in DB or \nPress Enter to Skip this Step")
	#Enter user info or just press enter to skip the step and show db content
	c=input(":-> ")
	if c=="":
		break
	else:
		if c.isdigit():
			user_inf['username']=input("\nEnter Username: ")
			user_inf['password']=input("\nEnter Password: ")
			user_inf['password']=base64.b64encode(str.encode(user_inf['password'])) 
			#Encoding password in base64 
			cursor.execute("insert into Users (username,password) values(:username,:password)",
				user_inf)  
			#The sql insertion querry 
		else:
			print("\nInvalid Input! Try again!")

print("\n"*100) #Sort of Clear Screen

print("="*35)
print ("Users present in DB")
print("="*35)

file.commit()

cursor.execute("Select * from Users") #For Loading all rows

for user_info in cursor: # Traversing the list of tuple example -> [(column1,column2,column3)..]
	print ("\nid :",user_info[0])	
	print ("username :",user_info[1])
	print ("password: ",str(base64.b64decode(user_info[2]),encoding="utf-8"))
	print ("password (stored): ",user_info[2])

file.close() # Cause it matters

print("\n")
print("="*35)
print ("Program Terminated!")  #End of Program
print("="*35)
