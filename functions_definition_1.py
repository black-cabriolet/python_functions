#this is a function definition

#the below function is going to compute the total.

def say_my_name(name):
    print(name)
say_my_name(input('Enter your name .'))
"""
The above function say_my_name has an argument (name) that takes input
from the user during the function calling and outputs the user's input.
"""


def sum(a,b):
    c = a+b
    return c
total = sum(int(input('Enter the value of a')),int(input('Enter the value of b')))
print(total)
"""
The above defined function sum() takes in two arguments (a,b) the in the functons body
c=a+b is returned.
A variable named total is assigned the function sum and the value of a and b is dependant 
on the users input. 
"""

#DEFINE A FUNCTION NAMED bigger_guy THAT TAKES IN TWO NUMBERS THEN OUTPUTS THE LARGER ONE.

def bigger_guy(a,b):
    """
    The below code is meant to return the greater number between a and b .However it has an error and it's not working
     as I intended it to work.So i commented it out then wrote the working code below the one that has the error.
    """

    #if a > b:
        #print(a)
    #elif a < b:
     #   print(b)
    #else:
     #   exit("Sorry we don't recognize that")
    if a > b:
        return a
    else:
        return b


bigger_guy2 = bigger_guy(int(input("Enter the value of a")),int(input("Enter the value of b")))
print(f"This is the value of Bigger_guy2 {bigger_guy2}")


#THIS IS THE CONCEPT OF USING LAMBDA.
#HOW DOES LAMBDA WORK
"""
lambda argument1,argument2:expression(argument1 + argument2)     
"""
    #EXAMPLE 1
sum2 = lambda a,b:a+b
"""
lambda takes only one equation and therefore assummes it and auto returns it..

"""
print(sum2(3,3))

    #EXAMPLE 2
greet = lambda greet,name:f"{greet} {name}"
print(greet('Hello','Tyreek'))

        #ASSERT TESTING(How to test your code)
def test_sum():
    assert sum(1,2 == 3)
    assert sum(-20,20)== 0
    assert sum(560,780) == 1340
    print("Sum Function :All Tests Passed 100%")
"""
(assert) is used to check there is any error in the code that I am writing.
The above code asserts the sum function that we defined above checking if the code is working as 
it is supposed to be.>>IN THE SUM FUNCTION THAT WE DEFINED ABOVE ,WE SAID THAT >>>
            def sum(a,b):
                c = a+b
                return c
>>>IN THE assert sum(-20,20)== 0        >>> -20+20 == 0 >>>>this tests if the sum functio works properly."""

test_sum()


