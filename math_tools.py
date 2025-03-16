def add(a,b):
    '''returns the sum of a and b'''
    return a+b

def subtract(a,b):
    '''returns the difference between a and b'''
    return a-b

def multiply(a,b):
    '''returns the product of a and b'''
    return a*b

def divide(a,b):
    '''returns the quotient of a divided by b'''
    if b== 0:
        print('Cannot divide by zero')
    else:
        result = a/b
    return result
    