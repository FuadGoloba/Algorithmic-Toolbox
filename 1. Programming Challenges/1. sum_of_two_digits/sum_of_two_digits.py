# Sum of Two Single Digits

def sum_of_digits(first_digit, second_digit):
    """Compute the sum of two single digit numbers.
    Input: Two single digit numbers.
    Output: The sum of these numbers."""

    return first_digit + second_digit

if __name__ == "__main__":
    a,b = map(int, input().split())
    print(sum_of_digits(a,b))