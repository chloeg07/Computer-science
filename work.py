#program to demonstrate basic string operations

#initialise the string
pangram = "the quick brown fox jumps over the lazy dog!"
#          01234567890123456789012345678901234567890123
# INDEXING
print(pangram[0])
print(pangram[1])
print(pangram[2+4])
print(pangram[14])
print(pangram[8])
print(pangram[43])

# the index can be any valid Python expression
pos= 17
print(pangram[pos])
print(pangram[pos+1])

#a general pattern used to find the last character
print( pangram[len(pangram)-1] )
