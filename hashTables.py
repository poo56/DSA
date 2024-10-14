#calculating the hash code
hash_set = [None, 'poo',None,'pete','poo']
def hash_function(value):
    sum_of_char_value = 0
    for char in value:
        sum_of_char_value += ord(char)
        #ord() function is used to get the Unicode code point of a single character.
    return sum_of_char_value % 10
    #assuming the size of length of the list is 10
#print("Poo has the hash code", hash_function("Poo"))

# Looking up a name using the hash function
def contains(name):
    index = hash_function(name)
    return hash_set[index] == name

print("poo is in the hash set:", contains('poo'))





