# Implementing a naive algorithm to compute the last digit of sum of squares of fibonacci numbers

def last_digit_of_sum_of_squares_of_fibonacci_numbers_naive(n):

    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fib = [0, 1]
    fib_sq = [0, 1]

    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]))
        fib_sq.append(fib[i] ** 2)

    return sum(fib_sq) % 10
    #return sum(f ** 2 for f in fib) % 10



# ---------------------------------------------------------------------------------------------------------------------------------------------------#

def last_digit_of_sum_of_squares_of_fibonacci_numbers_fast(n):

    """
        sum of squares of fibonacci numbers = F(n) * F(n + 1)
                                            = last digit of nth fibonacci number * last digit of (nth fibonacci number + 1) 
        Therefore last digit of sum of squares of fibonacci numbers = ( F(n) * F(n + 1) ) % 10
    """
    assert 0 <= n <= 10 ** 18
    return (last_digit_of_fibonacci_number(n) * last_digit_of_fibonacci_number(n + 1)) % 10
    

def last_digit_of_fibonacci_number(n):
    if n <= 1:
        return n

    period = get_pisano_period(10)
    n = n % period

    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 10)
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
    input_n = int(input())
    #print(last_digit_of_sum_of_squares_of_fibonacci_numbers_naive(input_n))
    print(last_digit_of_sum_of_squares_of_fibonacci_numbers_fast(input_n))

