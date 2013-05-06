#Count the number of iterations it takes to stop.

#1st exercise
#return number in sequence
def seq3np1_count(n):
    """ Prints the number of iterations for the 3n+1 sequence to stop."""

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
    
seq3np1_count(3)