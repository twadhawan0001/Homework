#Homework #6
# 1 Prime Clusters
# You have obtained a dataset of star temperatures from different stellar clusters.
# For your research, you are interested only in clusters where at least one star’s
# temperature is a prime number. Given a 2D NumPy array, write a function to
# find the rows where at least one value is a prime number. For example:
# >>> arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
# >>> containsPrimes(arr)
# array([[2, 3, 5],
# [11, 13, 17],
# [7, 10, 13]])
import numpy as np 
import math
arr1 = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])

def is_prime(n):
    if n <= 1:
        return False  # Primes are greater than 1
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3
    
    # Check for factors from 5 to √n, skipping even numbers
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False  # Found a divisor, not prime
    
    return True  # No divisors found, it's prime



def containsPrimes(arr):
    arr2 = np.array()
    for element in arr:
        for number in element:
            if is_prime(number) == 'True':
                arr2.append(element)
                