#3
#Write a Python program to solve the general version of the above problem.
#Ask the user for the time now (in hours), and ask foro the number of hours to wait.
#Your program should output what the time will be on the clock
#when the alarm goes off.

#input number, returns string
time = input("What time is it?")
print(type(time))

#need to turn time into an int before performing operations on it
print('The time on the clock will be', int(time) % 12, "o'clock")

#things that don't work:
#time = input("What time is it?")
#'not all arguments converted during string formatting'

#print('The time on the clock will be ', time+1, "o'clock")
#Can't convert 'int' object to str implicitely'


# **questions**

# when you print the type, is says "class: ____"  What's the class?
