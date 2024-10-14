#calculating the hash code

def hash_function(value):
    sum_of_char_value = 0
    for char in value:
        sum_of_char_value += ord(char)
        #ord() function is used to get the Unicode code point of a single character.
    return sum_of_char_value % 10
    #assuming the size of length of the list is 10
print("Poo has the hash code", hash_function("Poo"))
