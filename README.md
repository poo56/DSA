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
