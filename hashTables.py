#calculating the hash code
my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hash_function(value):
    sum_of_char_value = 0
    for char in value:
        sum_of_char_value += ord(char)
        #ord() function is used to get the Unicode code point of a single character.
    return sum_of_char_value % 10
    #assuming the size of length of the list is 10
#print("Poo has the hash code", hash_function("Pooe"))

#Adding the value for names in the Hash Set
def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)

# Looking up a name using the hash function
def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')

print(my_hash_set)
print("contains Stuart:",contains('Stuart'))





