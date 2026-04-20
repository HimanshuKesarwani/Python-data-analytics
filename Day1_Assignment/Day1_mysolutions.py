#1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.
from Day1_Assignment.NP_Day1_Notes import company

weight = input("Enter your weight (in kgs): ")
height = input("Enter your height (in meter): ")


BMI = float(weight)/(float(height)**2)

print(BMI)

#2- write a program which takes the name of the user as input and replace all the occurence of character 'a' in the name to 'b' and print it.

name = input("Enter your name: ")
print(name.replace('a','b'))

#3- write a program which takes 2 inputs from user as principle amount (int) and rate of annual interest (float) and print the expected total amount  after  2 years.
p = int(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))

SI = (p*r*2)/100
print(p+SI)

#4- write a program which takes city name from user input. irrespective of in which case user enters the city name, print the city name in camel case meaning first letter should be capital and rest in small.
city = input("Enter the city name: ")
print(city[0].upper()+city[1:].lower())

#5- write a program which takes the name of the user as input and print the index of character 'a' in the string. if 'a' is not there then return -1.
name = input("Enter your name: ")
index = name.find('a',0,len(name)-1)

print(index)

#6-  Display the number of letters in the below string
#my_word = "antidisestablishmentarianism"

my_word = "antidisestablishmentarianism"
print(len(my_word))

#7- take 3 inputs from user : first name , last name and age . Display the information in below format
'''exmaple 
first name : MOhit
last name : sharma 
age 32
Display : my name is Mohit Sharma and I am 32 years old.
note that first letter of first name and last name both should be in capital letters and rest in small. 
'''
fn = input('first name : ')
ln = input('last name : ')
age = input('age : ')

print(f"my name is {fn[0].upper()+fn[1:].lower()} {ln[0].upper()+ln[1:].lower()} and I am {age} years old.")

#8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
'''example 
first name : MOhit
last name : sharma 
company : infosys

Display : morma@infosys.com 

note full email id should -be in lower case'''

fin = input('first name : ')
lan = input('last name : ')
com = input('company : ')

#email_id = (fin[0:2]+lan[-3:]+"@"+com[0:]+".com").lower()

email_id = (f"{fin[0:2]}{lan[-3:]}@{com}.com").lower()
#both methods are correct any one can be used
print(email_id)






