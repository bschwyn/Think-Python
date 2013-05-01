#Repeat the call to seq3np1 using a range of values,
# up to and including an upper bound.

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


def seq3np1_range(upperbound):
   for i in range(1,upperbound+1):
       seq3np1_count(i)

seq3np1_range(8)