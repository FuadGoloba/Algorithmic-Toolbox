#python3

def polynomial_multiplication_naive(arr1, arr2):

    max_arr_len = max(len(arr1), len(arr2))

    product = []
    for i in range(max_arr_len + 1):
        product += [0]

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            product[i + j] = product[i + j] + (arr1[i] * arr2[j])
    
    return product


if __name__ == '__main__':
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print(polynomial_multiplication_naive(arr1, arr2))