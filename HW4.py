#HW 4
# 2.1 Making a List Variable
# Create a variable (name it anything you want, but make it descriptive!) that
# is assigned to a list with numbers 0 through 20. You should not write each
# number manually.
# >>> whateverNameYouWant = # Your code here
# >>> print(whateverNameYouWant)
# [0, 1, 2, ..., 20] # It should print all numbers 1-20 in a list

listtill20 = [] #initializing an empty list 
for i in range(0,21): #creating a for loop with range from 0 to 21, 21 being exclusive
    listtill20.append(i) #appending iterations of i to empty list
print(listtill20)

# 2.2 Working with List Elements
# Write a function that will take in your list from Part 2.1 and square each element
# in the list. Assign the result to a new variable.
# >>> whateverNameYouWant = # Your code from Part 2.1
# >>>
# >>> def squareList():
# >>> # Your code here
# >>>
# >>> anotherNameYouWant = squareList(list)
# >>> print(anotherNameYouWant)
# [0, 1, 4, ..., 400]

def squareList(list):
    '''squaring each element in list from 2.1 ranging from 0 to 20'''
    squares_l= [i**2 for i in listtill20]
    return squares_l
call_sq_list = squareList(listtill20)
print(call_sq_list)
# i encountered a error of squareList() takes 0 positional arguments but 1 was given; I fixed it by giving the function def an argument of "list"

# 2.3 Slicing
# Write a function that takes in your new list from Part 2.2 and returns the first
# 15 elements of the list using slicing.
# >>> anotherNameYouWant = squareList(list)
# >>> first_fifteen_elements(anotherNameYouWant)
# [0, 1, 4, ..., 196]

def first_fifteen_elements(squaredlist):
    '''this function returns the first 15 elements of the previous squared list through splicing'''
    spliced_sqlist = call_sq_list[0:15]
    return spliced_sqlist

print(first_fifteen_elements(call_sq_list))

# 2.4 Striding
# Write a function that takes in your list from Part 2.2 and returns every 5th
# element from the list using striding.
# >>> anotherNameYouWant = squareList(list)
# >>> every_fifth_element(anotherNameYouWant)
# [16, 81, 196, 361] 
def every_fifth_element(sqlist):
    '''will return every fifth element from a list'''
    sq_fifth_ele = call_sq_list[4::5]
    return sq_fifth_ele
print(every_fifth_element(call_sq_list))
# I wrote my code wrong so am getting 0,16,64,144,256,400; i changed the starting index to 4 to start at the 5th element: 16 and the stride to 5 

# 2.5 Slicing & Striding
# Write a function that takes your list from Part 2.2, slices the last 3 elements of
# the list, and then returns every 3rd element from that list in reverse order.
# >>> anotherNameYouWant = squareList(list)
# >>> fancy_function(anotherNameYouWant)
# [400, 289, 196, 121, 64, 25, 4]

def slicenrev(list):
    rev_sqlist = call_sq_list[20:0:-3]
    return rev_sqlist
print(slicenrev(call_sq_list))


# 3 2D lists
# 3.1 Creating a 5x5 2D List
# Write a function that uses nested for loops to create a 5x5 2D list where the
# numbers 1 through 25 are stored sequentially. Assign the result to a new vari-
# able.
# >>> matrix = create_2d_list()
# >>> print(matrix)
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
# [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

listtill25 = [] #initializing an empty list 
for i in range(1,26): #creating a for loop with range from 0 to 26, 26 being exclusive
    listtill25.append(i) #appending iterations of i to empty list
print(listtill25)    
    
def create_2d_list(list):
    matrix= []
    count = 1
    for i in range(5):
        row= []
        for j in range(5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix

twodmatrix = create_2d_list(listtill25)
print(twodmatrix)

# 3.2 Replacing 2D List with Multiples of 3
# With the 2D list you created in Part 3.1, write a function that will replace all
# multiples of 3 with the character “?”.
# >>> matrix = create_2d_list()
# >>> modified_2d_list(matrix)
# [[1, 2, ‘?’, 4, 5],
# [‘?’, 7, 8, ‘?’, 10],
# [11, ‘?’, 13, 14, ‘?’],
# [16, 17, ‘?’, 19, 20],
# [‘?’, 22, 23, ‘?’, 25]]

matrix = []
def modified_2d_list(matrix):
    for i in range(len(matrix)):  # Iterate through rows
        for j in range(len(matrix[i])):  # Iterate through columns
            if matrix[i][j] % 3 == 0:  # Check if multiple of 3
                matrix[i][j] = "?"  # Replace with "?"
    return matrix  # Return modified matrix

twodmodified = modified_2d_list(twodmatrix)
print(twodmodified)

# 3.3 Summing None-’?’ Elements
# Assign the result of your function from Part 3.2 to a variable. Write a function
# that will iterate through the new 2D list variable and return the sum of all the
# elements that are not “?”. Hint: Try using “!=”.
# >>> matrix = create_2d_list()
# >>> new_matrix = modified_2d_list(matrix)
# >>> sum_non_question_elements(new_matrix)
# 217

def sum_non_question_elements(new_matrix):
    total = 0
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if new_matrix[i][j] != '?':
                total += new_matrix [i][j]
    return total 

sum_matrix = sum_non_question_elements(twodmodified)
print(sum_matrix)