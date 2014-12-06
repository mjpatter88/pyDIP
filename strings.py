#!/usr/bin/python3
# Unicode is a system designed to represent every character from every language
# Unicode chars are 4 bytes, but various ways to "encode" them.
# UTF-32 - four bytes per character.
# UTF-16 - two bytes per character. (with hacks for characters past 65535)
# UTF-8 - variable-length encoding. ASCII chars take 1 byte, latin 2, etc.

# In Python 3, all strings are sequences of Unicode characters.
# You can turn these strings into UTF-8 bytes (or other encodings)
# Strings/characters are an abstraction. Bytes are not strings/characters.

name = 'Michael Patterson'
print(name)
print(len(name))
name += '7'
print(name)

username = 'mike'
password = 'anwiadbs'
print("{0}'s password is {1}.".format(username, password))
# You can also use "compound field names" with string formatting.
# This allows you to access elements in a list, a module's variables, etc.
# You can also use "format specifiers" much like printf() flags
print("{0:.1f} {1}".format(698.24, 'GB'))

longString = \
'''
This string will continue until another set of
triple quotes are found. 

I believe that the formatting
is also maintained including the new lines.
'''
print(longString)

# strings come with many utility functions like splitlines, lower, upper, etc.
stringA = "This is a sentence."
print(stringA[5:7])

# You can define byte objects by using a 'b'
bytesA = b'abcd\x65'
print(bytesA)
print(type(bytesA))

# Each byte within the byte object can either be an ASCII character (letter)
# or an  encoded hexadecimal number from \x00 to \xff

# byte objects are immutable, but you can convert to a bytearray if needed.

# You can't mix bytes and strings, but you can decode bytes to a string.
print(bytesA.decode('ascii'))
print(bytesA.decode('big5'))
# These happen to be the same since I use only ascii letters.


# Python 3 assumes that your source code is encoded in UTF-8.
# This can be changed by included an encoding declaration at the top of a file.





