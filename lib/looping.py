#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -=1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    # code goes here!
    return[x ** 2 for x in int_list]
print(square_integers([1, 2, 3, 4]))

def fizzbuzz():
    for i in range(1, 101):  # Loop through numbers from 1 to 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  # For multiples of both 3 and 5
        elif i % 3 == 0:
            print("Fizz")  # For multiples of 3
        elif i % 5 == 0:
            print("Buzz")  # For multiples of 5
        else:
            print(i)  # For all other numbers
print(fizzbuzz())
