#Homework 3
# 1 Oski Stole Your Power
# Oski hacked your computer and you can no longer use x**y or pow(x, y). Find
# a different way (by writing a function) that can compute x raised to the power
# of y.
# >>> x = 2
# >>> y = 3
# >>> computePower(x, y)
# 8
def com_power(x,y):
    #computes x raised to the power of y 
    power = x**y 
    return (print(power))
com_power(2,3)

# 2 What Should I Wear?
# You are trying to decide what to wear to the Python DeCal lecture, but you are only concerned about the day’s lowest and highest temperatures. Write a
# function that takes in a list as input and returns a tuple with the min and max as two values.
# (14, 28)

readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(readings):
    min_max_read = [min(readings), max(readings)]
    tup_mm = tuple(min_max_read)
    return (tup_mm)
temperatureRange(readings)

# 3 Check if its the Weekend
# All your classes have assigned problem sets due next week, and you want to
# check if it’s the weekend so you have time to work on them. Write a function
# that takes a day of the week (represented as an integer, where 1 = Monday, 2
# = Tuesday, etc) and returns True if its a weekend and False if otherwise.
# >>> day = 6 # Saturday
# >>> isWeekend(day)
# True
# 1
day= [1,2,3,4,5,6,7]
def wknd_check(day):
    return day==6 or day==7
wknd_check(5)

# 4 Fuel Efficiency Calculator
# The Python DeCal wants to take a trip to the Lick Observatory ( San Jose,
# CA) and they want to pick the best car. Write a function that takes the distance
# traveled (in miles) and the amount of fuel consumed (in gallons) as input and
# returns the fuel efficiency.
# >>> distance = 70 # miles
# >>> fuel = 21.5 # gallons
# >>> fuel_efficiency(distance, fuel)
# 3.26 
    
def fuel_efficiency(distance, fuel):
    return(distance/fuel)
fuel_efficiency(70, 21.5)

# 5 Secret Code
# Write a function that takes an integer as input and moves its last digit to the
# front of the number. You may NOT convert the input to a string. Hint: Try
# modulus (%) and floor division. (\\) to solve this problem.
# >>> n = 12345
# >>> decodeNumbers(n)
# 51234

# 6 Min & Max but with Loops!
# Oh no! Oski hacked you computer again... now you have lost the ability to use
# min() and max().
# 6.1 For Loops
# Write two functions to manually find the minimum and maximum values in a
# list of numbers with for loops.
# >>> nums = [2024, 98, 131, 2, 3, 72]
# >>> find_min_with_for_loop(nums)
# 2
# >>> find_max_with_for_loops(nums)
# 2024
nums = [2024, 98, 131, 2, 3, 72]
maxnum= nums[0] #initializing max
min_num = nums[0] #initializing min 
for i in nums:
   if i > maxnum:
       maxnum = i
   if i < min_num:
       min_num = i 

print("Max:", maxnum)
print("Min:", min_num)

# 6.2 While Loops
# Write two functions to manually find the minimum and maximum values in a
# list of numbers with while loops.
# >>> nums = [2024, 98, 131, 2, 3, 72]
# >>> find_min_with_while_loop(nums)
# 2
# >>> find_max_with_while_loops(nums)
# 2024

nums = [2024, 98, 131, 2, 3, 72]
def find_min(nums):
    if not nums:
        return None  # Handle empty list case
    
    min_val = nums[0]
    i = 1
    
    while i < len(nums):
        if nums[i] < min_val:
            min_val = nums[i]
        i += 1
    
    return min_val

def find_max(nums):
    if not nums:
        return None  # Handle empty list case
    
    max_val = nums[0]
    i = 1
    
    while i < len(nums):
        if nums[i] > max_val:
            max_val = nums[i]
        i += 1
    
    return max_val

print("Minimum:", find_min(nums))
print("Maximum:", find_max(nums))

# 7 Counting Vowels
# Write a function that takes a string as an input and returns the number of vowels
# in the string and the number of consonants in the string as tuple. Don’t forget
# about capital letters! Hint: You can use .isalpha() to check if a character is
# a letter.
# >>> text = "UC Berkeley, founded in 1868!"
# >>> vowel_and_consonant_count(text)
# (4, 11) --> there are 8 vowels in the string 
text = "UC Berkeley, founded in 1868!"

def vow_n_cons_ct(text):
    vowels = "aeiou"
    vow_ct = 0
    cons_ct = 0
    text = text.lower()
    for let in text:
        if let.isalpha():
            if let in vowels:
                vow_ct += 1
            else:
                cons_ct += 1
    return(vow_ct, cons_ct)

print(vow_n_cons_ct(text))

# 8 Calculate Digital Root
# Write a function that takes an integer as an input and returns the sum of its
# digits.
# >>> num = 2468
# >>> digital_root(num)
# 20
num = 2468
def digital_root(num):
    return sum(int(digit) for digit in str(num))

print(digital_root(num))
