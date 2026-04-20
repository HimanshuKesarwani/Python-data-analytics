from websocket import isEnabledForTrace

'''1- for the day 4 and day 3 assignments convert all the programs to functions'''

'''2- write a Python function which takes a positive number as input and return the factorial of the number.'''

def factorial(n):
    num=1
    for i in range(1,n+1):
        num *= i
    return num

n=int(input("Enter the number for factorial : "))
print(factorial(n))

'''
3- Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def count_letters(str):
    u,l=0,0
    for i in range(len(str)):
        if str[i].isupper():
            u+=1
        if str[i].islower():
            l+=1
    return u,l

x = input("Enter the string for counting Lowercase and uppercase : ")

print(f"No. of Upper case characters : {count_letters(x)[0]} \nNo. of Upper case characters : {count_letters(x)[1]} ")

'''
4- Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

'''

def removedup(x):
    return list(set(x)) #

x=list(map(int,input("Enter the elements of list").split(","))) #list(map(int,t) used to convert list of strings to list of integers

print(f"Unique List: {removedup(x)}")

'''
5- Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam.

'''

def check_pallindrome(x):
    return x.lower() == x[::-1].lower()

if check_pallindrome(input("Enter the string : ")):
    print("The string is Pallindrome")
else:
    print("The string is not a Pallindrome")


'''

6- Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

'''

def arrange(x):
    l=x.split("-")
    l.sort()
    return '-'.join(l) # '-'.join(list) converts list to a string with '-' delimiter

print(f"Expected Result : {arrange(input("Sample Items : "))}")


'''
7- write a python function that accepts a string and prints the count of occurence of each characters
sample string: aabccda
expected result:
a -> 3
b-> 1
c-> 2
d -> 1
'''

def count_occurence(x):
    y = list(set(x)) #converts string to set where repetition is not allowed
    y.sort()
    for i in range(len(y)):
        print(f"{y[i]} -> {x.count(y[i])}")

count_occurence(input("Sample string : "))

'''
8- write a function called is_prime that takes an integer as an argument and returns True if it is a prime number, and False otherwise.

'''

def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int((n)**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

print(f"{'Prime Number' if is_prime(int(input("Enter the number for checking prime : "))) else 'Not a Prime Number'}")


'''
9- write a function called generate_fibonacci that takes an integer n as input and returns a list of the first n Fibonacci numbers.
'''

def generate_fibonacci(n):
    flist=[1,1]
    if n == 1:
        return [1]
    else:
        for i in range(n-2):
            flist.append(flist[i]+flist[i+1])
    return flist

print(f"The fibonacci sequence : {generate_fibonacci(int(input("Enter the number for fibonacci sequence:")))}")


'''
10- Write a function called capitalize_odd_letters that takes a string as input and returns the same string with the odd-indexed letters capitalized.
'''

def capitalize_odd_letters(x):
    l=list(x)
    for i in range(len(l)):
        if (i+1)%2 != 0 :
            l[i]=l[i].upper()
    return ''.join(l)

print(capitalize_odd_letters(input("Enter the string : ")))


'''
11- write a function called find_common_elements that takes two lists as input and returns a new list containing the common elements between the two lists.
red,apple,banana,yellow,orange,berry
black,berry,apple,iphone,banana,wifi
'''

def find_common_elements(x,y):
    z=[]
    for element in x:
            if element in y:
                z.append(element)
    return z

print(find_common_elements(list(input("Enter the first list : ").split(',')),list(input("Enter the second list : ").split(','))))

