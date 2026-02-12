"""
Lab 6 - Selections and Iterations 
(100 marks in total, including 10 exercises)

Author:  <Kirti>
Due Date: This Friday (Feb. 13) 5pm.

Objective:
1. Practice coding simple Python functions and writing unit tests testing functions by assert
2. Practice how to operate on lists
3. Practice with iterations using loop
4. Practice using the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, etc. 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
5. Practice with selections, boolean expressions and boolean functions.
"""



"""
Exercise 1 (10 marks)

Implement a function is_in_list(nums, k) that checks 
whether the number k exists in the list nums.
If k is in nums, return True.
Otherwise, return False.
"""
def is_in_list(nums, k):                                                           # nums is the list and k is the number we are looking for in the list 
    for num in nums:                                                               # we loop through each number in the list nums and check if it is equal to k 
        if num == k:                                                               # if we find a number in the list that is equal to k then we return True 
            return True 
    return False                                                                   # if we finish looping through the list and we do no find k then we return False 
    

assert is_in_list([4, 5, 6], 5) == True
assert is_in_list([], 3) == False
assert is_in_list([-3, -2, -1, 0], -1) == True



"""
Exercise 2 (10 marks)

Write a function has_negative(nums)
that returns True if the list contains any negative number,
otherwise False.
"""

def has_negative(nums):                                                           # we have a list called nums and we want to check if there are any negative numbers in that list 
    for num in nums:                                                              # we loop through each number in the list nums and check if it is negative 
        if num < 0:                                                               # This means that if we find a number in list nums that is less than 0 then we return True because that means it is a negative number 
            return True 
    return False 

assert has_negative([1, 2, 3, -4, 5]) == True
assert has_negative([0, 2, 3, 4, 5]) == False


"""
Exercise 3 (10 marks)

Write a function all_even(nums) 
that returns True if all numbers in the list are even,
otherwise False.

"""

def all_even(nums):                                                               # we have a list called nums and now we want to check if all the numbers in that list are even 
    for num in nums:                                                              # We loop through each number in the list nums and check if it is even or not 
        if num % 2 !=0:                                                           # Here != means not equal to, so if we find a number in list nums that is not even then we return False because that means not all the numbers in the list are even 
            return False                                                          # the reason why i did not do == 0 is because if we do that then we would only be checking if the number is even and not checking if it is odd 
    return True 



assert all_even([2, 4, 6, 8]) == True
assert all_even([2, 3, 4]) == False


"""
Exercise 4 (10 marks)

Write a function count_even_odd(nums) that counts how many numbers
in a list are even and how many are odd. 

Return a list [even_count, odd_count]
"""
def count_even_odd(nums):                                                         # we have a list called nums and we want to count how many numbers in list nums are even and how many are odd 
    even_count = 0                                                                # we created a variable called even_count and it is 0 because we want to start counting from 0 and will update as we loop through nums list 
    odd_count = 0 
    for num in nums:                                                              # we loop through each number in the list nums and check if it is even or odd and update the even_count and odd_count variable accordingly 
        if num % 2 == 0:                                                          # This means we found a even number 
            even_count += 1                                                       # Now we update the even_count by adding 1 to it. the reason why we do += 1 is because we want to keep counting even number in list and if we just do = then we would only considering last even number and not all 
        else: 
            odd_count += 1 
    return [even_count, odd_count] 

assert count_even_odd([1, 2, 3, 4, 5, 6]) == [3, 3]
assert count_even_odd([2, 4, 6, 8]) == [4, 0]
assert count_even_odd([1, 3, 5]) == [0, 3]


"""
Exercise 5 (10 marks)

Write a function temp_category(temps) that
categorizes temperatures with an input of list of temperatures:

≥30 → "hot"

15-29 → "mild"

<15 → "cold"

Return a list [hot_count, mild_count, cold_count]

"""

def temp_category(temps):                                                           # we have a list called temps and we want to cateforize the temperatures in that list as hot, mild , cold and also count how many hot, mild and cold there are in the list and return a list with those counts 
    hot_count = 0                                                                   # we created these variables and set it to 0 because we want to start counting from 0 and will update as we loop through the list temps 
    mild_count = 0 
    cold_count = 0 
    for temp in temps: 
        if temp >= 30:                                                              # This means we found a hot temperature 
            hot_count += 1 
        elif temp >= 15:                                                            # This means we found a mild temperature because if it was hot then it would have been caught by first if statement 
            mild_count += 1 
        else: 
            cold_count += 1 
    return [hot_count, mild_count, cold_count]


assert temp_category([32, 28, 15, 12, 35]) == [2, 2, 1]
assert temp_category([10, 5, 0]) == [0, 0, 3]
assert temp_category([20, 25, 30]) == [1, 2, 0]




"""
Exercise 6 (10 marks)

Write a function mult_category(nums) that categorizes
each number in the list according to the following rules:

Multiple of 2 → append 2
Multiple of 3 → append 3
Multiple of 5 → append 5
If a number is not a multiple of 2, 3, or 5 → append the letter "O"

Return a list of the categories.
"""

def mult_category(nums):                                                           # we have a list called nums and we want to categorize each number in that list according to rules given and return a list of those categories                                       
    categories = []                                                                # we created an empty list called categories because we want to append the category of each number in list nums to this categories list and return it at the end. here append means that we want to add the category to the end of categories list and not replace the whole list with the category 
    for num in nums: 
        if num % 2 == 0: 
            categories.append(2)                                                   # This means we found a number that is a multiple of 2 and we append 2 to the categories list 
        elif num % 3 == 0:
            categories.append(3)                                                   # This means we found a number that is a multiple of 3 and we append 3 to the categories list 
        elif num % 5 == 0:
            categories.append(5)                                                   # Here append means that we want to add 5 to the end of categories list and not replace the whole list with 5. This means we found a number that is a multiple of 5 and we append 5 to the categories list 
        else: 
            categories.append("O")
    return categories 

assert mult_category([2, 3, 5, 7]) == [2, 3, 5, "O"]
assert mult_category([4, 9, 10, 11]) == [2, 3, 2, "O"]
assert mult_category([15, 7, 30, 11]) == [3, "O", 2, "O"]


"""
Exercise 7 (10 marks)

Implement a function to reverse a list.

"""
def reverse_list(nums):                                                              # we have a list called nums and we want to reverse that list and return the reveresed list 
    reversed_list = []                                                               # We start by empty list called reversed_list because we want to add the numbers from nums list to this reveresed_list in reverse order and return it at the end 
    for num in nums: 
        reversed_list.insert(0, num)                                                 # Here we are using insert function to add the number num to the index 0 of reversed_list. This means that each time we find a number in nums list we add it to the beginning of reversed_list and this way we are able to reverse the order of the numbers in nums list and store it in reverses_list 
    return reversed_list                                                             # What is insert function? The insert() method inserts an element to the list at a specified index. 
assert reverse_list([1, 3, 4]) == [4, 3, 1]                                          # The syntax is list.insert(index, element). Here index is the position where you want to insert the element and element is the value you want to insert. 
assert reverse_list([3, 9, 6]) == [6, 9, 3]


"""
Exercise 8 (10 marks)

Implement a function to remove duplicates from a list.

"""
def remove_duplicates(nums):
    unique_nums = []                                                                 # we have a list called nums and we want to remove the duplicates from list nums and return a list of unique numbers. We start by creating an empty list
    for num in nums: 
        if num not in unique_nums:                                                   # Here we are checking if the number num is not already in the unique_nums list. If it is not in the unique_nums list then we append it to the unique_nums list because that means it is a unique number and we want to keep it. If it is already in uniques_nums then we do not append it to list because it is duplicate and we want to remove it from list nums 
            unique_nums.append(num)
    return unique_nums 

assert remove_duplicates([1, 3, 3, 4]) == [1, 3, 4]
assert remove_duplicates([1, 1, 3, 4, 3]) == [1, 3, 4]


"""
Exercise 9 (10 marks)

Write a function my_factorial(n) that returns the factorial 
of a non-negative integer n.

Factorial rule:
0! = 1
1! = 1
n! = n * (n-1) * (n-2) * ... * 1

You may assume n >= 0.

"""
def my_factorial(n):                                                                   # we have a non-negative integer n and we want to return the factorial of n. we can use the accumulator algorithm pattern to solve this problem. 
    factorial = 1 
    for i in range(1, n+1):
        factorial *= i 
    return factorial 

assert my_factorial(0) == 1
assert my_factorial(1) == 1
assert my_factorial(3) == 6
assert my_factorial(5) == 120

"""
Exercise 10 (10 marks)

Write a function my_fib(n) that returns a list containing the first n Fibonacci numbers.

Fibonacci rule:
Start with [0, 1]
Each next number is the sum of the previous two
If n = 1, return [0]
If n = 2, return [0, 1]
If n = 3, return [0, 1, 1]
If n = 4, return [0, 1, 1, 2]
"""
def my_fib(n):
    if n == 1: 
        return [0]
    elif n == 2: 
        return [0, 1]
    else: 
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_fib)
        return fib_sequence 

assert my_fib(1) == [0]
assert my_fib(2) == [0, 1]
assert my_fib(5) == [0, 1, 1, 2, 3]
assert my_fib(7) == [0, 1, 1, 2, 3, 5, 8]

"""
Congratulations on finishing your lab6!
Now upload to your GitHub repository, and paste your GitHub link on e-learn.

Have a great reading break!
"""