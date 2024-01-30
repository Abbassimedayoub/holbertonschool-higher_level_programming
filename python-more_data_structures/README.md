# Python More Data Structures: Set and Dictionary

This module provides implementations and examples for two important data structures in Python: Set and Dictionary.

## Set

A Set is an unordered collection of unique elements. It supports various mathematical operations like union, intersection, difference, and symmetric difference. In Python, sets are implemented using the `set` data type.

### Usage

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)

# Removing elements from a set
my_set.remove(3)

# Set operations
union_set = my_set.union({4, 5, 6})
intersection_set = my_set.intersection({5, 6, 7})
```
## Dictionary
A Dictionary is an unordered collection of key-value pairs. Each key must be unique, and it maps to a specific value. Dictionaries are implemented using the dict data type in Python.
### Usage 

```pyhton 
# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values in a dictionary
name = my_dict['name']
age = my_dict.get('age')

# Adding or updating key-value pairs
my_dict['gender'] = 'Male'

# Removing a key-value pair
del my_dict['city']

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
```



## Authors

- [@abbassimedayoub](https://www.github.com/abbassimedayoub)


