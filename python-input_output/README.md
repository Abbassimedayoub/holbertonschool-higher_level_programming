# Python - Input/Output

## Input

1. Using input() function
- This function allows you to take input from the user via the command line.
- Example

 ```python
name = input("Enter your name: ")
print("Hello, " + name)
```


2. Reading from files
- You can read input from files using functions like open() and various file reading methods (read(), readline(), readlines()).
- Example


```python
with open('input.txt', 'r') as f:
    lines = f.readlines()
```

## Output
1. Printing to the console
- You can use the print() function to output data to the console.
- Example:

```python
print("Hello, world!")
```

2. Writing to files
- You can write data to files using functions like open() with mode 'w' or 'a', and various file writing methods (write(), writelines()).
- Example
  
```python
with open('output.txt', 'w') as f:
    f.write("This is some data written to the file.")
```
## Formatting Output
1. Using string formatting
- You can use string formatting techniques like % formatting, .format() method, or f-strings (Python 3.6+).
- Example

```python
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")
```
2. Formatting options
- You can format output using various options like padding, precision, alignment, etc.
- Example:
```pyhton
num = 3.14159
print("Pi: {:.2f}".format(num))  # prints Pi: 3.14
```
 
- These are some basic concepts of input/output handling in Python. Depending on your requirements, you can explore more advanced techniques and libraries like csv, json, or pickle for structured data handling, or os and sys modules for system-level input/output operations.
