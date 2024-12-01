# Hash Table

It is a data structure used to insert, look-up and remove key-value pairs quickly. 
 1. In Hash Table data is stored in the Array format where each data value has its own unique index value.
 2. Accessing the Data becomes quick and easy if we know the index of the desired data.
 3. Fast retrieval of the data no matter how much the data is present. 

## Application or the Use Cases
 1. Database Indexing
 2. Caching
 3. Error checking
 4. Compliers
 5. Passowrd Authentication

## Hashing Algorithm or the Hash Function
1. Calculation of applied to a key to transform it into an address
2. For numeric keys, divide key by the number of available address n and take the reminder
   Address = key % n
3. For Alphanumeric caulculate the sum of the ASCII code mod size of the array
   index number = Sum of the ASCII code  % size of the array

## Types of Collisions in a Hash Table

Collision in Hashing:

1. Hash functions are designed to distribute keys uniformly across the hash table, but since the table has a finite number of slots (buckets), multiple keys can hash to the same slot, resulting in a collision.
2. Load Factor: The load factor is the ratio of the number of elements to the size of the hash table. A higher load factor increases the likelihood of collisions, so it's important to maintain a low load factor for optimal performance.

In this article, we focus on the strategy of separate chaining. Here is how it works overall.

Essentially, the primary storage underneath a HashSet is a continuous memory as Array. Each element in this array corresponds to a bucket that stores the actual values.

Given a value, first we generate a key for the value via the hash function. The generated key serves as the index to locate the bucket.

Once the bucket is located, we then perform the desired operations on the bucket, such as add, remove and contains.
<img width="256" alt="image" src="https://github.com/user-attachments/assets/d8b5ea4c-c651-45f0-9e01-f8235eb87da2">



     class MyHashSet:
         def __init__(self):
             """
             Initialize your data structure here.
             """
             self.keyRange = 769
             self.bucketArray = [Bucket() for i in range(self.keyRange)]
     
         def _hash(self, key):
             return key % self.keyRange
     
         def add(self, key):
             """
             :type key: int
             :rtype: None
             """
             bucketIndex = self._hash(key)
             self.bucketArray[bucketIndex].insert(key)
     
         def remove(self, key):
             """
             :type key: int
             :rtype: None
             """
             bucketIndex = self._hash(key)
             self.bucketArray[bucketIndex].delete(key)
     
         def contains(self, key):
             """
             Returns true if this set contains the specified element
             :type key: int
             :rtype: bool
             """
             bucketIndex = self._hash(key)
             return self.bucketArray[bucketIndex].exists(key)
     
     class Node:
         def __init__(self, value, nextNode=None):
             self.value = value
             self.next = nextNode
     
     class Bucket:
         def __init__(self):
             self.head = Node(0)
     
         def insert(self, newValue):
     
             if not self.exists(newValue):
                 newNode = Node(newValue, self.head.next)
                 #set new head
                 self.head.next = newNode
     
         def delete(self,value):
             prev= self.head
             curr = self.head.next
             while curr is not None:
                 if curr.value == value:
                     prev.next = curr.next
                     return
                 prev = curr
                 curr = curr.next
     
         def exists(self,value):
             curr = self.head.next
             while curr is not None:
                 if curr.value == value:
                     return True
                 curr = curr.next
     
             return False

        

