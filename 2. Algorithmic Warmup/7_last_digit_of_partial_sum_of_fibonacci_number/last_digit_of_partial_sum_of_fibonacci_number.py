# Implementing a naive algorithm to compute the last digit of partial sum of fibonacci numbers from m to n

def last_digit_of_partial_sum_of_fibonacci_numbers_naive(start, end):
    """
        Given inputs start, and end, compute the last digit of sum of fibonacci numbers from start to end

        start
        end

    """
    assert 0 <= start <= end <= 10 ** 18
    if end <= 1:
        return end

    fib = [0] * (end + 1) # Create a list to store previous Fibonacci numbers
    fib[0] = 0
    fib[1] = 1
    for i in range(2, end + 1): # Compute all Fibonacci numbers up to end and store in list
        fib[i] = fib[i - 1] + fib[i - 2]

    return sum(fib[start:]) % 10 # Compute the sum of fibonacci numbers from start to end and return the last digit



# ------------------------------------------------------------------------------------------------------------------------------------------#

# Implementing a fast algorithm to compute the last digitof the sum of fibonacci numbers of n (O(logn))


def last_digit_of_partial_sum_of_fibonacci_numbers_fast(start, end):
    """
        Given inputs start, and end, compute the last digit of sum of fibonacci numbers from start to end more efficiently.

        start : start offibinacci number
        end : end of nth fibonacci number

        This algorithm works as thus;
            1. Compute the sum of fibonacci numbers from 0 to N
            2. Compute the sum of fibonacci numbers from 0 to (M - 1)
            3. Compute the last digit of (step 2 - step 1)

        Note: To compute the sum of fibonacci numbers:
            F(n) = Fibonacci numbers of n
            S(F(n)) = Sum of Fibonacci numbers of n ; eg S(F(4) = F(0) + F(1) + F(2) + F(3) + F(4)
            The sequences of F(n) and S(F(n)) are related as thus; S(F(n)) = F(n+2) - 1; e.g F(4) = 3; F(6) = 8; S(F(4)) = 7

            Given the above: Therefore, Last digit of sum of fibonacci number = (F(n+2) - 1) mod 10

            Recall that the nth Fibonacci modulo m (i.e Fib_mod(n, m)) is periodic 
            such that Fib_mod(2000, 10) or Fib(2000) % 10 = Fib(2000 % 60) % 10 = Fib(20) % 10 
            i.e The last digits repeats themselves with a period of 60 (which is the Pisano period); eg. pisano period of 3 is 8, etc

            Therefore the last digit of sum of fibonacci number Using Pisano period = (F((n+2)mod 60) - 1) mod 10

    """
    assert 0 <= start <= end <= 10 ** 18
    start = start - 1
    return  ((last_digit_of_fibonacci_number((end + 2) % get_pisano_period(10)) - 1)  - (last_digit_of_fibonacci_number((start + 2) % get_pisano_period(10)) - 1)) % 10


def last_digit_of_fibonacci_number(n):
    if n <= 1:
        return n

    fib = [0, 1] # list to store fibonacci numbers
    for i in range(2, n + 1): # Loop through n
        fib.append((fib[i - 1] + fib[i - 2]) % 10) # Compute the fibonacci of each number till n
    return fib[n]


def get_pisano_period(m):
    current = 0
    nxt = 1
    period = 0
    while True:
        old_nxt = nxt
        nxt = (current + nxt) % m
        current = old_nxt
        period += 1
        if current == 0 and nxt == 1:
            return period

if __name__ == "__main__":
    input_m, input_n = map(int, input().split())
    #print(last_digit_of_partial_sum_of_fibonacci_numbers_naive(input_m, input_n))
    print(last_digit_of_partial_sum_of_fibonacci_numbers_fast(input_m, input_n))
