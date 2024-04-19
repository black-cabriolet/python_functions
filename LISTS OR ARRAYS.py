            ###LISTS
#APPLICATIONS OF LISTS
          # (1)NETFLIX-used to show a list of movies and series either vertically or horizontaly
          # (2)ONLINE MARKETING APPS/WEBSITES - used to show a list of products or items or services
#EXAMPLE 1
#methods - list.append() >>.append is a method
#functions - print() >>print() is a function
#methods vs functions
fruits = ['Apple','Orange','Pineapple','Blueberry']
print(fruits)

"""
append is used to add a value to the end of the first list/array
"""
fruits.append('Banana')
print(fruits)
fruits.append('Strawberry')
print(fruits)

    ##INDEXING
"""
Indexing in Python is a way to refer the individuals items within an 
iterable by its position."""
#In Computers items are identified using index from 0 - 9
#In ARRAYS the first item has an index of 0,the second item 1

print(f"{fruits[0]}")
print(f"{fruits[3]}")
#print(f"{fruits[9]}")
"""
line 29 is going to be an error because our list doesn't have up 
to that range.So the error is going to be the one below.
>>>> LIST INDEX OUT OF RANGE  >>>>>"""

#HOW TO LIST THE LAST ITEM
"""
In order to list the last item in a list WE ARE ALLOWED TO GO BACKWARDS IN 
PYTHON by using NEGATIVE INDEX"""
#EXAMPLE
print(f"{fruits[-1]}")
"""line 40 is going to give us the last item in the list .If we were to 
say -2 then we would get the second last item in out list."""



                ##THE FOLLOWING IS USED TO MAKE A LIST FROM STRINGS##
#.split()--->>converts strings to items in a list
print(f"my name is Tyreek".split())
"""
What this does is it will split the words and make a list/array out of each word in the sentence.It will identify the space or any marking that u desire .
---->>>OUTPUT----->>>>['my', 'name', 'is', 'tyreek'].This is a new list create from the string.If i had said .SPLIT(,) this would have splited the sentence where it identified the commas and any marking i may have specified in the .split() function
"""
print('my name is tyreek'.split())

def count_words(phrase):
    return len(phrase.split())

print(count_words("my  name is tyreek"))