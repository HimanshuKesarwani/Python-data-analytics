'''
1- given a list of numbers, write a program to find the mean of the numbers in list
'''
from unicodedata import unidata_version

list=[1,2,3,4,5]
print(f"mean : {sum(list)/len(list)}")

'''
2- given a list of numbers unsorted, write a program to find the median of the numbers in list
'''

list=[3,4,1,2,8,9,7,10,5]
list.sort()
print(list)
if len(list)%2==0 :
    median=(list[(len(list)-1)//2] + list[((len(list)-1)//2)+1])//2
    print('even terms',median)
else :
    median=list[(len(list))//2]
    print('odd terms',median)

'''
4- create a dictionary to store following attributes of CSK 
key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players), oppenont name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss

'''

ipl = {
    "CSK":{
    "Name":"Chennai Super Kings","Captain":"MSD",
    "Players":["MSD", "Gaikwad", "Conway", "Ashwin", "Jadeja", "Dube", "Curran", "Hooda", "Shankar", "Overton", "Patel"],
    "Opponents":["MI","RCB","GT"],
    "Result":"Won"
    }
}

print(ipl["CSK"]["Opponents"][2])

'''
5- in the previous dictonary add one more item for RCB. you can choose any 3 opponents.
'''

ipl["RCB"]={
    "Name":"Royal Challengers Bangalore","Captain":"Kohli",
    "Players":["Kohli", "Salt", "Patidar", "Livingstone", "Sharma", "David", "Pandya", "BKumar", "Hazelwood", "Shepherd", "Dayal"],
    "Opponents":["MI","CSK","GT"],
    "Result":"Loss"
    }

print(ipl)

'''
6- write a program to take a positive number as input from user. if the user enters negative number then keep promting him to enter positive number until he enters the positive number and then print the same

'''

n=0
while n <= 0 :
    n=int(input("Enter a positive number : "))
print(n)

'''
7- consider the below list of list conatins following information :

1. The name of a university 
2. The total number of enrolled students
3. The annual tuition fees

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

write a program to print follwoing information :
1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
2- total number of student entrolled in all the unversities together 
3- mean of tuition fees
'''

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

uni_name = []
stu_enrolled = 0
tot_fees = 0
for i in range(len(universities)) :
    uni_name.append(universities[i][0])
    stu_enrolled += universities[i][1]
    tot_fees += universities[i][2]
print(f"List of all universities : {uni_name} \nTotal Students Enrolled : {stu_enrolled} \nAverage fees : {tot_fees/len(universities)}")


'''
8- write a program to convert above universities list to a dictionary. the keys should be the name of the university

'''

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
uni_dict={}
for i in range(len(universities)) :
    uni_dict[universities[i][0]] = [universities[i][1],universities[i][2]]
print(uni_dict)

#Alternate Method (similar to List Comprehension method)
uni_dict={universities[i][0]: [universities[i][1],universities[i][2]] for i in range(len(universities))}
print(uni_dict)

'''
9-  write a program that reverses a given string. For example, if the input is "Hello" from user, the output should be "olleH"

'''

str="Hello"
print(str[::-1])

'''
10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.

'''

list=[3,4,1,2,8,9,7,10,5]
print(max(list))
