#Write a function, is_prime, which takes a single integer argument
# and returns True when the argument is a prime number
# and False otherwise.

def is_prime(p):
    q = 2
    while q < p:
        if p % q !=0:
            q = q+1
        else:
            return False
    return True
    
for i in range(2,10):
    print(i,is_prime(i))