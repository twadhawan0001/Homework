#Homework #6
# array([[2, 3, 5],
# [11, 13, 17],
# [7, 10, 13]])
import numpy as np 
import math

arr1 = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    mask = np.apply_along_axis(lambda row: any(is_prime(num) for num in row), axis=1, arr=arr)
    return arr[mask]

print(containsPrimes(arr1))

# #2.1
def checkerboard():
    return np.zeros((8, 8), dtype=int)
print(checkerboard())

# #2.2
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1  # Fill 1s at even rows, even columns
    return board

print(checkerboard())

# #2.3

def checkerboard_3():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board
print(checkerboard_3())               

# #2.4
def reverse_checkerboard():
    board = checkerboard_3()  # Get the normal checkerboard
    return 1 - board  # Flip 1s to 0s and vice versa
print(reverse_checkerboard())

# # #3 The Expanding Universe
universe = np.array(['galaxy', 'clusters'], dtype=str)
def expansion(iterable, number):
    separator = " "*number
    return (np.char.join(separator, iterable))

print(expansion(universe, 10))

# # 4 Second-Dimmest Star
np.random.seed(123)
stars = np.random.randint(500, 2000, (5,5))

def secondDimmest(array):  
    sorted_array = np.sort(array, axis=0)  # Sort each column
    return sorted_array[1, :]  # Select the second smallest value in each column

print(secondDimmest(stars))  # Print result



        