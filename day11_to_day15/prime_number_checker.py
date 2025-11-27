"""Prime Number Checker:
You need to write a function called is_prime() that checks whether if the number
passed into it is a prime number or not.  It should return True or False."""

def is_prime(num):
    if num <= 1:
        return False
    
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    
    if num % 1 == 0 and num % num == 0:
        return True
    else:
        return False
        
        
        
print(is_prime(75))
    