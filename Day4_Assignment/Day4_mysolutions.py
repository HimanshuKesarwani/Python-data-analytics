'''
1- create a txt file and put 4-5 lines. Now create another file from the previous file and at the end of each line put the count of words.

example :
file 1:
this is namaste sql course
this is python course
this assinment is part of day4 lecture


file2:this is namaste sql course:5
this is python course:4
this assignment is part of day4 lecture:7

'''
import random

#This part of code write the content in main file
with open("1question.txt",'w') as f:
    f.write("this is namaste sql course \nthis is python course \nthis assignment is part of day4 lecture \n")

#This part copies the content along with word length for each line in copy file
try:
    with open("1question.txt",'r') as f1, open("1question_copy.txt", 'w') as f2:
        for line in f1:
            f2.write(f"{line[:-2]}:{len(line.split())} \n") #line[:-2] done to remove new line problem
except FileNotFoundError:
    print(f"Error: Source file 1question.txt not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#This part shows the content of copy file
with open("1question_copy.txt", 'r') as f3:
    print(f3.read())


'''
2- given below dictonaries of states and their capital:

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

pick a state from above dictonary and ask user to enter the capital of the state.If the user answers incorrectly, then repeatedly ask them
for the capital until they either enter the correct answer or type "exit".
If the user answers correctly, then display "Correct" and end the program. However, if the user exits without guessing correctly, display
the correct answer and the word "Goodbye".

Note: Make sure the user isn’t punished for case sensitivity. In other words, a guess of "Denver" is the same as "denver". Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".

'''

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

import random
key=random.choice(list(capitals_dict.keys()))

val1 = capitals_dict[key]
val2 = ''

while val1.lower() != val2.lower() :

    val2 = input(f"Enter the correct capital of {key} or EXIT : ")
    if val1.lower() == val2.lower() :
        print('Correct')
        break
    if val2.lower() == 'exit' :
        print('Goodbye')
        break

'''
3- write a program to take state as input from user and print the capital of the state using above dictonary. If the state is not there in dictonary then print "sorry , information not available"
'''


capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

state = input("Enter the name of State : ")

try:
    capital = capitals_dict[state[0].upper()+state[1:].lower()]
    print(capital)
except KeyError:
    print("sorry , information not available")

'''

4- Let say You have one 100 cats.
One day, you decide to arrange all your cats in a giant circle. Initially,none of your cats has a hat on.
You walk around the circle a 100 times, always starting with the first cat (cat #1). 
Each time you stop at a cat, you check if it has a hat on. If it doesn’t, then you put a hat on it. If it does, then you take the hat off.

1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you stop only at every second cat (#2, #4, #6,
#8, and so on).
3. The third round, you stop only at every third cat (#3, #6, #9, #12,
and so on).
4. You continue this process until you’ve made one hundred rounds
around the cats. On the last round, you stop only at cat #100.

'''

list_cats = [False]*100
#print(list_cats)

d=1

for i in range(0,100):
    for j in range(d-1,100,d):
        if list_cats[j]:
            list_cats[j]=False
        else:
            list_cats[j]=True
    d+=1
print(f"Cats with hats on their head: {sum(list_cats)}")
print(list_cats)



'''An optimised version for the above program can be via just counting the perfect squares between 0 to 100
   Below is the explanation of above problem - 

We have 100 cats arranged in a circle, initially all without hats. We perform 100 rounds of walking around the circle, starting each round at cat #1. In each round, we interact with certain cats based on the round number:

Round 1: Stop at every cat (1, 2, 3, ..., 100). For each, if no hat, put one on; if has a hat, take it off.

Round 2: Stop at every second cat (2, 4, 6, ..., 100).

Round 3: Stop at every third cat (3, 6, 9, ..., 99).

...

Round 100: Stop only at cat #100.

After completing all 100 rounds, we need to determine how many cats have hats on their heads.

Observing the Process
Let's think about what happens to a single cat, say cat #k, over all the rounds.

In which rounds will we stop at cat #k?

We stop at cat #k in round d if d divides k (i.e., k is a multiple of d).

For example, for cat #6:

Round 1: 6 is a multiple of 1 → stop

Round 2: 6 is a multiple of 2 → stop

Round 3: 6 is a multiple of 3 → stop

Round 6: 6 is a multiple of 6 → stop

Other rounds like 4,5,7,... do not divide 6, so no stop.

So, the number of times we stop at cat #k is equal to the number of divisors of k.

Determining the Hat Status
Each time we stop at a cat, we toggle its hat status:

No hat → put hat on

Has hat → take hat off

Initially, all cats have no hats. So, the final hat status of cat #k depends on how many times we toggled its hat:

If the number of toggles is even, the cat ends up with no hat (since even toggles cancel out: on→off→on→off...).

If the number of toggles is odd, the cat ends up with a hat (on→off→on).

From the above, the number of toggles is the number of divisors of k.

So, cat #k ends up with a hat if k has an odd number of divisors.

Numbers with Odd Number of Divisors
Now, the key question is: which numbers between 1 and 100 have an odd number of divisors?

Normally, divisors come in pairs. For example:

10: divisors are 1 & 10, 2 & 5 → total of 4 (even).

9: divisors are 1 & 9, 3 & 3 → but 3 is repeated, so total is 3 (odd).

The numbers that have an odd number of divisors are the perfect squares. This is because for a perfect square, one of its divisors is repeated (like 3 for 9).

For non-square numbers, all divisors can be paired uniquely, leading to an even count.

Counting Perfect Squares up to 100
Now, let's list the perfect squares between 1 and 100:

1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
6² = 36
7² = 49
8² = 64
9² = 81
10² = 100

So, there are 10 perfect squares between 1 and 100 (from 1² to 10²).
'''

