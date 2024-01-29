# Python - Data Structures: Lists, Tuples

This directory contains examples and explanations of two fundamental data structures in Python: Lists and Tuples. These data structures are used to organize and manipulate collections of data efficiently.
## Lists
### Overview
A list is a mutable, ordered collection of elements, and it allows for dynamic resizing. Lists are defined using square brackets [].
### Exemple
``` python
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_list[0]
last_element = my_list[-1]

# Slicing
subset = my_list[1:4]

# Modifying elements
my_list[2] = 10

# Adding elements
my_list.append(6)
my_list.extend([7, 8, 9])

# Removing elements
removed_element = my_list.pop(2)
my_list.remove(5)

# Finding elements
index_of_element = my_list.index(4)
element_count = my_list.count(8)
```
### Methods
1. append(): Adds an element to the end of the list.
2. extend(): Appends the elements of an iterable to the end of the list.
3. pop(): Removes and returns the element at the specified index.
4. remove(): Removes the first occurrence of a specified element.
5. index(): Returns the index of the first occurrence of a specified element.
6. count(): Returns the number of occurrences of a specified element.
## Tuples
### Overview
A tuple is an immutable, ordered collection of elements. Once a tuple is created, its size and content cannot be changed. Tuples are defined using parentheses ().

### Exemple
``` pyhton
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
first_element = my_tuple[0]
last_element = my_tuple[-1]

# Slicing
subset = my_tuple[1:4]

``` 
### Methods
Understanding and mastering Python's lists and tuples are crucial for efficient data manipulation. Lists are versatile and allow dynamic changes, while tuples provide immutability, ensuring data integrity in certain scenarios. Choose the appropriate data structure based on the requirements of your program.
## Conclusion
Understanding and mastering Python's lists and tuples are crucial for efficient data manipulation. Lists are versatile and allow dynamic changes, while tuples provide immutability, ensuring data integrity in certain scenarios. Choose the appropriate data structure based on the requirements of your program.


## Authors

- [@abbassimedayoub](https://www.github.com/abbassimedayoub)






