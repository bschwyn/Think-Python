#keep track of the maximum number of iterations


import turtle

def seq3np1_count(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""

    count = 1 
    while n != 1:
        count = count + 1
        #print(n)
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    #print(n)                  # the last print is 1
    print(count)
    return count

wn=turtle.Screen()        
line=turtle.Turtle()

line.penup()
line.goto(-200,-200)
line.pendown()

def linegraph(upperbound):
    maxSoFar = 0
    for i in range(1,upperbound+1):
        sq=seq3np1_count(i)
        y=sq*20-200
        x=i*20-200
        line.goto(x,y)
        line.stamp()
        line.write('  '+str(sq))
        if sq > maxSoFar:
            maxSoFar = sq
    print('the max is ',maxSoFar)
    
        
       
     
linegraph(20)
