'''
1- write a program which takes single input from user contaning first name,last name and age as comma separated value and display then in 3 lines in given format below.

example user input : Ankit,Bansal,35

output:
First name is Ankit
last name is Bansal
Ankit is 35 years old

note : do not hardcode name at any place
'''

user = input("Enter name, surname and age: ")
ul = user.split(",")
print(f"First name is {ul[0]} \nlast name is {ul[1]} \n{ul[0]} is {ul[2]} years old ")

'''
2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]

combined the 2 list and diplay the same without using extend method
'''
list1 = [1,3,4]
list2 = [2,4,6]

list3 = list1 + list2
print(list3)

'''
3- given a list list1=[1,2,3,4,5,6,7,8]
diplay a new list which contains only odd position index values from above list.
'''

list1=[1,2,3,4,5,6,7,8]
list2=list1[1::2]
print(list2)


'''
4- ipl= ['CSK','MI','KKR','LSG','PBKS']

take a ipl team name as input from user and display a list of all elements from that name.

example : input : KKR
output : ['KKR','LSG','PBKS']

'''

ipl = ['CSK','MI','KKR','LSG','PBKS']
x = input("input : ")
#print(type(x))
i = ipl.index(x)
#print(type(i))
print(f"output : {ipl[i:]}")

'''

5- ipl= ['CSK','MI','KKR','LSG','PBKS']

take a ipl team name as input from user and display a list of all elements except input one

example : input : KKR
output : ['CSK','MI','LSG','PBKS']

'''

ipl = ['CSK','MI','KKR','LSG','PBKS']
x = input("input : ")
ipl.pop(ipl.index(x))
print(f"output : {ipl}")

'''

6- ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . replace the index element of list with new value and display the same

example : input : 2,SRH
output : ['CSK','MI','SRH','LSG','PBKS']

'''

ipl = ['CSK','MI','KKR','LSG','PBKS']
x,d = input("input : ").split(",")
#print(type(x),type(d))
ipl[int(x)] = d
print(f"output : {ipl}")

'''

7- ipl= ['CSK','MI','KKR','LSG','PBKS']
take ipl team name as user input. display True if the team exists else display False.

'''

ipl= ['CSK','MI','KKR','LSG','PBKS']
x = input('input : ')
print(x in ipl)

'''

8-ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list. 
Display the old list , new list,length of original and new list

example : input : 2,SRH
output : 
old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6
'''

import copy
ipl = ['CSK','MI','KKR','LSG','PBKS']
x,d = input("input : ").split(",")
ipl_copy=copy.deepcopy(ipl)
ipl_copy.insert(int(x),d)
print(f"old list : {ipl} and length {len(ipl)} \nnew list : {ipl_copy} and length {len(ipl_copy)} ")



