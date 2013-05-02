#Use the turtle graphics to graph the number of iterations.
#You will probably want to use setworldcoordinates to make your graph an appropriate scale.
#You should also use the turtle to write out the loop variable and the number of iterations
#if the number of iterations is more than 100.

import turtle

def seq3np1_count(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""

    count = 1 
    while n != 1:
        count = count + 1
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(count)

#def seq3np1_range(upperbound):
 #  for i in range(1,upperbound+1):
  #     seq3np1_count(i)

wn=turtle.Screen()        
line=turtle.Turtle()

def linegraph(upperbound):
	line.penup()
	line.goto(-100,-100)
	line.pendown()
	for i in range(1,upperbound+1):
        x=20

		line.goto(x,y)

seq3np1_count(1)
seq3np1_count(2)
seq3np1_count(3)
seq3np1_count(4)
seq3np1_count(5)

linegraph(5)
    

wn.exitonclick()

