import math_tools
f_num= float(input("Enter the first number:"))
s_num= float(input("Enter the second number:"))
choice_op = input('Which operation do you want to perform(add, subtract, multiply or divide)?')

if choice_op == 'add':
    print(math_tools.add(f_num, s_num))
elif choice_op == 'subtract':
    print(math_tools.subtract(f_num, s_num))
elif choice_op == 'multiply':
    print(math_tools.multiply(f_num, s_num))
elif choice_op == "divide":
    print(math_tools.divide(f_num, s_num))
else:
    print('This is not a valid function.')
    