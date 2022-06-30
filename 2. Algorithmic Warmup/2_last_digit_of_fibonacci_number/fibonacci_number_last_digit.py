# Implementing a naive algorithm to compute the last digit of nth fbonacci number

def fib_last_digit_naive(n):
    
    if n <= 1:
        return n
    
    return (fib_last_digit_naive(n - 1) + fib_last_digit_naive(n - 2)) % 10
    
    
# Implementing a fairly efiicient algorithm to compute the last digit of nth fbonacci number

def fib_last_digit_fast(n):
    
    fib = [0, 1]
    if n <= 1:
        return n
    
    for i in range(2, n + 1):
        fib.append(((fib[i - 1]) + fib[i - 2]) % 10)
        
    return fib[n]

if __name__ == "__main__":
    input_n =int(input())
    print(fib_last_digit_fast(input_n))