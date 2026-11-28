
def is_prime(n):
    if n < 2:                       
        return False
    for i in range(2, n):
        if n % i == 0:             
            return False            
    return True                     

def primes_up_to(n):
    primes = []
    for number in range(2, n + 1):
        if is_prime(number):        
            primes.append(number)
    return primes

print(is_prime(1))                  
print(is_prime(29))                 
print(primes_up_to(20))  