#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
def counter():
    user_input_1 = int(input('Please input a number between 1 and 100: '))
    user_input_2 = int(input('Please input a second number between 1 and 100: '))
    if user_input_1 < user_input_2: 
        while user_input_1 < user_input_2 +1:
            print(user_input_1)
            user_input_1 += 1
    elif user_input_1 > user_input_2:
         while user_input_1 + 1 > user_input_2:
             print(user_input_2)
             user_input_2 += 1
        
    

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
def reverse_input():
    user_input_str = str(input('Please enter a value to reverse: '))
    user_input_list = [*user_input_str]
    reversed_list = user_input_list[::-1]
    reversed_str = ''.join(reversed_list)
    print(reversed_str)
    
#txt = 'jungle'
#splt = txt.split()
#print([*txt])



'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''


'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''


'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''


'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''


'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''



'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''



'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
