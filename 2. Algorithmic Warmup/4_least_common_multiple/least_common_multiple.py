# The least common multiple LCM(a,b) of two positive integers a and b is the smallest integer m that is divisible by both a and b.
#Compute the least common multiple of two integers 1≤a,b≤2⋅109.


#How LCM(a,b) is related to GCD(a,b)?


def lcm_naive(a, b):
    """Naive algorithm to compute the least common multiple of two integers"""
    
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    # Initialise multiple to be the max of a and b
    multiple = max(a, b)
    # Increment multiple until we find a multiple that can divide both numbers and leave no remainder
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1
        
    return multiple

def lcm_naive2(a, b):
    
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    # Loop through the product of a and b and return a number that divides both a and b without a remainder else return the product of a and b
    for n in range(max(a, b), a*b + 1):
        if n % a == 0 and n % b == 0:
            return n
        
    return a * b

# Implementing a more efficient solution than the naive solution that does not have to loop through all possible numbers of a * b
#How LCM(a,b) is related to GCD(a,b)?
def lcm_fast(a , b):
    """The LCM and GCD of two numbers are somewhat related as lcm(a,b)= |ab| / gcd(a,b) """
    
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    
    return (a * b) // gcd(a, b)

def gcd(a, b):        
    if b == 0:
        return a
    
    return gcd(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm_fast(a, b))
