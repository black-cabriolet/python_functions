# #map anf filter
#
#                 ###  MAP  ##
#
# """
# -->>Map in python is a function that works as an iterator to  return a result after applying a function to every item of an iterable.
# -->>Map()function takes two inputs as a function and an iterable object.The function that is given to map() is a normal function, and it will iterate over all the values present in the
# iterable object given.
# """
#
# def double_number(number):
#     return number * 2
# print(list(map(double_number , [1,2,3])))#call the list function on the map to be able to iterate and print each item inside. This will print ia list/array
#
#
#                 ###   FILTER    ##
#
# """
# -->>The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# """
#
# numbers = [1,2,3,4,5,6,7,8,9]
# """
# the codes below will pick even numbers from the list that is given
# """
# print(list(filter(lambda number: number % 2 == 0,numbers)))
#
#
#                 ##LIST_COMPREHENSION     ###
# """
# this will select and display the even numbers
# """
#
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# #filte for even numbers
# print([number for number in numbers if number % 2 == 0])
#
# #filter for double numbers
# print([number * 2 for number in numbers ])
#
# #filter for odd numbers
# print([number for number in numbers if number % 3 == 0])

from flask import render_template_string