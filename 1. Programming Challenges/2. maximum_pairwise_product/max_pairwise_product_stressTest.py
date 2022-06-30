# Stress Testing algorithm to find the maximum product of 2 distinct numbers in a sequence of non -ve integers

import random
from max_pairwise_product_Fast import max_pairwise_product_Fast
from max_pairwise_product_Naive import max_pairwise_product_Naive

def stressTest(N, M):
    
    """ N: Max number of length of sequence
        M: Max number of sequence of numbers"""
    
    while True:
        # generating a random integer between 2 and N (since n >= 2 for the max_pairwise_product algorithm)
        n = random.randint(2, N)
        
        # Allocating an array between 0 and M
        arr = [random.randint(0, M) for i in range(n)]
        print(arr)
        
        res1 = max_pairwise_product_Naive(arr)
        res2 = max_pairwise_product_Fast(arr)
        
        if res1 != res2:
            print("Wrong", res1, res2)
            break
        else:
            print("OK")
            #return
        
if __name__ == "__main__":
    N = int(input())
    M = int(input())
    
    print(stressTest(N,M))
