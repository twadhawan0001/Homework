# 1.1. pwd
# 2. ls 
# # 3. cd ../brianna_repo; brianna_repo % git pull origin main
# 4. brianna_repo % cp -r homework/ ~/python_decal/judy_decal/homework/
# 5. nano homework.py
# 6. nano homework.py
# 7. To save the file, you do Control + O and then control + x on windows. Then do git add; git commit -m "adding homework"; git push origin master
# 8. Judy cannot make changes to Brianna's version of the file. She must create a copy of Homework.py on her local computer by using "git pull origin main" on the Homework directory from brianna_repo
# 9. cd ~/Recent/
# Question 2:
# 2.1: 
def checkDataType(data):
    datatype = (type(data))
    return datatype
print(checkDataType('3'))

#2.2: 
def evenOrOdd(integer):
    if integer %2 == 0:
        result = ('Even')
    else:
        result = ('Odd')
    return result 
print(evenOrOdd(13))

3: Loops
numbers = [1,2,3,4,5]
def sumWithLoop(numbers):
    count = 0
    for i in numbers:
        count += i
    return count 
print(sumWithLoop(numbers))

# 4.1 Lists
listt = ['a', 'b', 'c']
def duplicateList(inputlist):
    dup_list = []
    for i in inputlist:
        dup_list.append(i)
        dup_list.append(i)
    return dup_list
print(duplicateList(listt))

# 4.2 Debugging
def square(num):
    return num * num
print(square(5))
# there was a missing colon after the argument in the definition.


# 5 HW2 Review: Git
#Added




        