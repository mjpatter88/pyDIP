#!/usr/bin/python3

################################# os module examples ##########################
import os
cur_dir = os.getcwd()
print(cur_dir)

# It's ok to use linux style pathnames here even on windows.
os.chdir('/home/michael')
print(os.getcwd())
os.chdir(cur_dir)

# You don't have to put in the slash, python will add the right type for you
print(os.path.join('/home/michael', 'work'))
print(os.path.expanduser('~'))

pathname = '/home/michael/work/pyDIP/humanSize.py'
print(os.path.split(pathname))
print(os.path.splitext(pathname))

import glob
print(glob.glob('*.py'))

print(os.stat('humanSize.py'))
print(os.path.realpath('humanSize.py'))



######################### List Comprehension Examples ##########################

# "A list comprehension provides a compact way of mapping a list into another
# list by applying a function to each of the elements of the list."

listA = [1, 3, 5, 7, 9]
listB = [num * 2 for num in listA]
print(listA)
print(listB)

# It may be helpful to read the comprehension right to left. 
# "in listA look at each num and apply "num*2" to that num.

fileList = [os.path.realpath(f) for f in glob.glob('*.py')]
print(fileList)


######################### Dict Comprehension Examples ##########################

# Very similar to the above list comprehensions, but you enclose the expression
# in curly braces and you provide two expressions separated by a colon to be
# applied to each item.

meta_data = {f:os.stat(f) for f in glob.glob('*.py')}
print(meta_data)

# Quick way to swap the keys and values of a dictionary.
# Only works when the values are immutable since they become the new keys.
dictA = {'a':1, 'b':2, 'c':3}
dictB = {value:key for key, value in dictA.items()}
print(dictA)
print(dictB)

# You can also do set comprehension, which is very similar
setA = {x ** 2 for x in range(10)}
print(setA)




