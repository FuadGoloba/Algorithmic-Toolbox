# Fibonacci numbers are defined recursively: F0=0, F1=1, and Fn=Fn−1+Fn−2 for n≥1. This definition results in the recursive function compute_fibonacci_number_naive

def fibonacci_number_naive(n):
    assert 0 <= n <= 45
    
    if (n <= 1):
        return n
    
    return fibonacci_number_naive(n-1) + fibonacci_number_naive(n-2)


# Implementing a more efficient solution as the naive solution is rather slow as n gets bigger (n>=40)

cache = {0:0, 1:1}

def fibonacci_number(n):
    assert 0 <= n <= 45
    
    if n in cache:
        return cache[n]
    
    result = fibonacci_number(n-1) + fibonacci_number(n-2)
    cache[n] = result
    
    return result

if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))    