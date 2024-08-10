# Basic arithmetic operations
a = 10
b = 3

# Addition
sum_result = a + b
print("Sum:", sum_result)  # Output: Sum: 13

# Subtraction
sub_result = a - b
print("Subtraction:", sub_result)  # Output: Subtraction: 7

# Multiplication
mul_result = a * b
print("Multiplication:", mul_result)  # Output: Multiplication: 30

# Division (float)
div_result = a / b
print("Division (float):", div_result)  # Output: Division (float): 3.3333333333333335

# Floor Division (integer)
floor_div_result = a // b
print("Floor Division:", floor_div_result)  # Output: Floor Division: 3

# Modulus (remainder)
mod_result = a % b
print("Modulus:", mod_result)  # Output: Modulus: 1

# Exponentiation (power)
exp_result = a ** b
print("Exponentiation:", exp_result)  # Output: Exponentiation: 1000


# Basic list operations
my_list = [1, 2, 3, 4, 5]

# Accessing elements by index
first_element = my_list[0]
print("First Element:", first_element)  # Output: First Element: 1

# Slicing a list
sub_list = my_list[1:4]
print("Sub-list:", sub_list)  # Output: Sub-list: [2, 3, 4]

# Appending an element to the list
my_list.append(6)
print("List after append:", my_list)  # Output: List after append: [1, 2, 3, 4, 5, 6]

# Removing an element from the list
my_list.remove(3)
print("List after removal:", my_list)  # Output: List after removal: [1, 2, 4, 5, 6]

# Length of the list
list_length = len(my_list)
print("Length of the list:", list_length)  # Output: Length of the list: 5


# Basic string operations
my_string = "Hello, World!"

# String length
string_length = len(my_string)
print("String Length:", string_length)  # Output: String Length: 13

# Accessing a character by index
first_char = my_string[0]
print("First Character:", first_char)  # Output: First Character: H

# Slicing a string
sub_string = my_string[7:12]
print("Sub-string:", sub_string)  # Output: Sub-string: World

# Converting to uppercase
upper_string = my_string.upper()
print("Uppercase String:", upper_string)  # Output: Uppercase String: HELLO, WORLD!

# Replacing a substring
replaced_string = my_string.replace("World", "Python")
print("Replaced String:", replaced_string)  # Output: Replaced String: Hello, Python!

# Splitting a string into a list
split_list = my_string.split(", ")
print("Split List:", split_list)  # Output: Split List: ['Hello', 'World!']


# Basic dictionary operations
my_dict = {"name": "John", "age": 25, "city": "New York"}

# Accessing a value by key
name = my_dict["name"]
print("Name:", name)  # Output: Name: John

# Adding a new key-value pair
my_dict["email"] = "john@example.com"
print("Dictionary after addition:", my_dict)
# Output: Dictionary after addition: {'name': 'John', 'age': 25, 'city': 'New York', 'email': 'john@example.com'}

# Removing a key-value pair
del my_dict["age"]
print("Dictionary after deletion:", my_dict)
# Output: Dictionary after deletion: {'name': 'John', 'city': 'New York', 'email': 'john@example.com'}

# Length of the dictionary
dict_length = len(my_dict)
print("Length of the dictionary:", dict_length)  # Output: Length of the dictionary: 3


# Basic tuple operations
my_tuple = (10, 20, 30, 40, 50)

# Accessing elements by index
second_element = my_tuple[1]
print("Second Element:", second_element)  # Output: Second Element: 20

# Slicing a tuple
sub_tuple = my_tuple[1:4]
print("Sub-tuple:", sub_tuple)  # Output: Sub-tuple: (20, 30, 40)

# Length of the tuple
tuple_length = len(my_tuple)
print("Length of the tuple:", tuple_length)  # Output: Length of the tuple: 5


# Basic set operations
my_set = {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)
print("Set after addition:", my_set)  # Output: Set after addition: {1, 2, 3, 4, 5, 6}

# Removing an element from the set
my_set.remove(3)
print("Set after removal:", my_set)  # Output: Set after removal: {1, 2, 4, 5, 6}

# Checking membership
is_member = 4 in my_set
print("Is 4 in the set?:", is_member)  # Output: Is 4 in the set?: True
