            ###LISTS/ARRAYS
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
fruits.append('Banana')#this has made the use of a method called append.
print(fruits)#this has made the use of a function called print()
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

print(f"{fruits[0:3]}")
print(f"{fruits[0:4]}")
"""
The above code is used to display items in a list .'0:3' means that the items
with the following index from 0-2 will be displayed.
Suppose we said [0:4] then this would meand items with the index 0-3 

"""

print(len(fruits))
"""
The obove function LEN() is used to dispaly the length of items in a list .
In my list I have 6 items so the output will be 6
"""
#print(fruits[0:len(fruits) -2])
print(fruits)
"""
The code above will print the entire items in my list.I have 6 items in my list."""

        ### SLICING TECHNIQUES IN ARRAYS
#Used to slice anything in alist or even a string like in the example below.
print("Hi my name is Tyreek"[-1])
print("Hello Harry ,have you got a new hat today?"[0:7])
print(len("Hello my name is Tyreek"))
"""
The above code is using slicing technique to slice the string and get a particular character i.e
    (1)the last character in our case.
    (2)The first 6 characters in the string .NOT INCLUDING SPACE
Line 67 is using the len()function to display the length of the string listed.
"""

print(fruits[::-1])
"""
The above code is used to reverse the items in a list .
Starting from the last to the first.This uses the order of 1:meaning that it items after an interval of 1"""
print(fruits[::-2])
"""
The above code is used to reverse the items in alist using an interval or 2 beginning fron the last to first.
Takes the last (-1) then jumps (-2) and picks (-3)
"""


        ###SETS###
"""
The term sets is used to give a unique value out of a set that has similar values.

"""

    #EXAMPLE
list1 =[1,2,3,1,2,3,4,5,6,2,3,45,7,8,9]
list2 = [11,12,13,12,14,15,17,77,77,88,88,]
list3 =  list1 +list2
print(list3)
"""
the code in line 96 will print anything that is in list3 which is a combination of list2 and list1.
"""
print(set(list3))
"""
the code in line 100 will print only the unique numbers that are found in the list3 which is a combination of list2 and list 3
"""
list1.append(99)
print(len(set(list3)))

print(set(list1))

            ##THE FOLLOWING IS USED TO MAKE A LIST FROM STRINGS##
            # .split()--->>converts strings to items in a list
            ######SPLIT MEETHOD########


"""
SPLIT() - this method splits a string into a list .You can specify the separator ,default separator is any whitespace.

"""
#EXAMPLE 1
print(len('my name is tyreek'.split()))
"""
The split function has split the string above by identifying the whitespaces and spliting them at the whitespaces.
The len() is used to find the length/number of items in the string and in this case the length is 4
>>>>>['my', 'name', 'is', 'tyreek']
"""


#EXAMPLE 2
print(len('age,gender,name,location'.split(",")))
"""
The split function has just split the string by identifying the commas 
>>>>>['age', 'gender', 'name', 'location']
"""


print(f"my name is Tyreek".split())
"""
What this does is it will split the words and make a list/array out of each word in the sentence.It will identify the space or any marking that u desire .
---->>>OUTPUT----->>>>['my', 'name', 'is', 'tyreek'].This is a new list create from the string.If i had said .SPLIT(,) this would have splited the sentence where it identified the commas and any marking i may have specified in the .split() function
"""
print('my name is tyreek'.split())

def count_words(phrase):
    return len(phrase.split())

print(count_words("my  name is tyreek"))


                    ####this is a function that will take the list that is given the doubles @ of the items in the list then displays it out####
def double(numbers:list):
    """
    this line is for defining the funtion and then asssigning it arguments.The argument in the case is NUMBERS:LIST meaning that the argument should be a list and not any other data type
    """
    result = []
    """
    This is our empty array that is going to be appnended everytime
    """
    for number in numbers:
        result.append(number * 2)
    return result
    """
    if u use print at the end of function definition to display the results then to call the function u don't use print ]
    but u just call on the function by itself.
    if u use return at the end of function definition to display the results then to callthe function we use print(FUNCTION NAME)
    """
print(double([1,2,3,5]))

