# question1
def cube(base):
    result = base ** 3
    print(f'The cube of {base} is: {result}')


cube(3)

# What are the local variables of cube()?
# result, base

# result is the local variable 

# What will happen if we try to access result? Why?
# print(result)

# What happens and why?
# error, result is local to the func

# What will happen if we try to access base? Why?
# print(base)

# global variables at the top of the file


# Question2
name = "CS 1.1"

def welcome_class():
    # Is name a global var here?
    print(f'Welcome {name}!')
    # yes

def dismiss_class():
    # Is name a global var here?
    print(f'Goodbye {name}!')
      # yes

def print_name(name):
    # Is name a global var here? 
    print(f'Class Name: {name}')
      # yes

def change_name():
    # Is name a global var here?
    name = 'CS 1.0' 
    return name
    # no its local 
    # print(f'New Name: {name}')

welcome_class()
dismiss_class()
print_name("web2.0")
print(name)
name = change_name()
# Try uncommenting each line below and running the script


# What do you think will print?

# it will print name: webpage2.0

# print(name)

# Examine the code here figure out the scope of name
# Will the below code work? Why/Why not?
# no because name is not defined a second time within the scope
name ="James"
def add_year(name): 
    
    # Is name a global var here?
    # no
    name = name + ' 2021'
    print(f'New Name: {name}')






# for/if variable practice
# Here i is defined and initialized by the for loop
for i in range(1,10):
    print(f"i: {i}")


print(i)
 # is i "visible" here?  yes

import random


# Here a is defined and initialized inside the if and the else blocks
if random.random() < 0.5:
    a = 'Hello'
else:
    a = 'Goodbye'


print(a) # Is a visible outside of the if else block? no 

# n is a parameter variable that is defined when the count function is called
def count_to(n):
    for i in range(1, n):
        print(f"i: {i}")
        print(i)


count_to(5)


print(n) 
# is n "visible" here? 
# no. n is not defined in the code therefor it is not visable 
print(i) 
# what about i ? 
# i is visible 

