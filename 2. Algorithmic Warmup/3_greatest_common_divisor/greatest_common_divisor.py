# Implementing a naive algorithm that computes the greates common divisor between 2 numbers

def gcd_naive(a, b):
    
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    
    # Loop through the smallest number between a and b and return the number that divides both a and b
    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        
    assert False
    
# Implementing an efficient algorithm to compute the greatest common divisor between 2 numbers
# Here, We use Euclid's algorithm where the greates common divisor of numbers (a, b) is also the greatest common divisor of (a % b, b)
# e.g gcd(12, 8) = gcd(12 % 8, 8) = gcd(8, 12 % 8) = gcd(4, 8) which is 4

def gcd_fast(a, b):
    
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9
    # Recursively compute the gcd(a,b) till b becomes 0
    
    # base case
    if b == 0:
        return a
    return gcd_fast(b, a % b)
    
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_fast(a, b))
    
    