# Implementing a naive algorithm to compute the last digit of the sum of fibonacci numbers of n (O(n))

def last_digit_of_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fib = [0, 1] # list to store fibonacci numbers
    for i in range(2, n + 1): # Loop through n
        fib.append(fib[i - 1] + fib[i - 2]) # Compute the fibonacci of each number to n
    return sum(fib) % 10 # compute the last didgit of the sum of fibonacci numbers to n


# Implementing a fast algorithm to compute the last digitof the sum of fibonacci numbers of n (O(logn))

def last_digit_of_sum_of_fibonacci_numbers_fast(n):
    """
        F(n) = Fibonacci numbers of n
        S(F(n)) = Sum of Fibonacci numbers of n ; eg S(F(4) = F(0) + F(1) + F(2) + F(3) + F(4)
        The sequences of F(n) and S(F(n)) are related as thus; S(F(n)) = F(n+2) - 1; e.g F(4) = 3; F(6) = 8; S(F(4)) = 7

        Given the above: Therefore, Last digit of sum of fibonacci number = (F(n+2) - 1) mod 10

        Recall that the nth Fibonacci modulo m (i.e Fib_mod(n, m)) is periodic 
        such that Fib_mod(2000, 10) or Fib(2000) % 10 = Fib(2000 % 60) % 10 = Fib(20) % 10 
        i.e The last digits repeats themselves with a period of 60 (which is the Pisano period); eg. pisano period of 3 is 8, etc

        Therefore the last digit of sum of fibonacci number Using Pisano period = (F((n+2)mod 60) - 1) mod 10
        
    """
    return (last_digit_of_fibonacci_number((n +2) % get_pisano_period(10)) - 1) % 10
    
def get_pisano_period(m):
    '''
        Function to compute the pisano period of a fibonacci sequence

        m: number 
    '''
    current = 0
    nxt = 1
    period = 0
    while True:
        old_nxt = nxt
        nxt = (current + nxt) % m
        current = old_nxt
        period = period + 1
        if current == 0 and nxt == 1:
            return period

def last_digit_of_fibonacci_number(n):
    if n <= 1:
        return n

    fib = [0, 1] # list to store fibonacci numbers
    for i in range(2, n + 1): # Loop through n
        fib.append((fib[i - 1] + fib[i - 2]) % 10) # Compute the fibonacci of each number till n
    return fib[n]


if __name__ == "__main__":
    input_n = int(input())
    #print(last_digit_of_sum_of_fibonacci_numbers_naive(input_n))
    print(last_digit_of_sum_of_fibonacci_numbers_fast(input_n))

