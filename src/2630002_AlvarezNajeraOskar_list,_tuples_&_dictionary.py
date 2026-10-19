# ============================================================
# Student: Oskar Tadeo Alvarez Najera
# Student ID: 2630002
# Group: IM 1-1
# Subject: Python Strings
# ============================================================

# EXECUTIVE SUMMARY
# A list stores items in order and can be changed after it is created.
# A tuple also stores items in order, but it cannot be changed after creation.
# A dictionary stores information as key-value pairs, such as a product and its price.
# Lists are mutable, which means items can be added, removed, or replaced.
# Tuples are immutable, which makes them useful for fixed data such as coordinates.
# Dictionaries make it easy to find a value when its key is known.
# This file contains six practical problems using lists, tuples, and dictionaries.
# Each problem documents its inputs, outputs, validations, and three test cases.
# The examples include a shopping list, coordinates, a product catalog, grades,
# word frequencies, and a simple contact book.

# ------------------------------------------------------------
# Problem 1: Shopping list basics (list operations)
#
# Description:
# Create a shopping list from a comma-separated string, add one new item,
# display the total number of items, and search for a requested item.
#
# Inputs:
# - Initial items separated by commas.
# - One new item to add.
# - One item to search for.
#
# Outputs:
# - Items list, total items, and whether the search item was found.
#
# Validations:
# - The initial text, new item, and search item must not be empty.
# - Spaces around each item are removed.
# - If the initial list is invalid, the problem is skipped.
#
# Test cases:
# 1) Normal: "apple, banana, orange"; add "grape"; search "banana" -> Found: True.
# 2) Border: "apple"; add "apple"; search "pear" -> 2 items; Found: False.
# 3) Error: empty initial text -> Error: invalid input.
# ------------------------------------------------------------

print("\\n=== Problem 1: Shopping List Basics ===")
initial_items_text = input("Enter initial items separated by commas: ")

if initial_items_text.strip() == "":
    print("Error: invalid input")
else:
    items_list = []
    input_items = initial_items_text.split(",")

    for item in input_items:
        clean_item = item.strip()
        if clean_item != "":
            items_list.append(clean_item)

    if len(items_list) == 0:
        print("Error: invalid input")
    else:
        new_item = input("Enter a new item: ").strip()
        search_item = input("Enter an item to search for: ").strip()

        if new_item == "" or search_item == "":
            print("Error: invalid input")
        else:
            items_list.append(new_item)
            is_in_list = search_item.lower() in [item.lower() for item in items_list]
            print("Items list:", items_list)
            print("Total items:", len(items_list))
            print("Found item:", is_in_list)


# ------------------------------------------------------------
# Problem 2: Points and distances with tuples
#
# Description:
# Store two 2D points in tuples, calculate the Euclidean distance,
# and create a tuple containing the midpoint between the two points.
#
# Inputs:
# - Four numeric coordinates: x1, y1, x2, and y2.
#
# Outputs:
# - Point A, Point B, distance, and midpoint.
#
# Validations:
# - All four coordinates must be convertible to float.
# - If any coordinate is invalid, show an error message.
#
# Test cases:
# 1) Normal: A=(0, 0), B=(3, 4) -> Distance: 5.0; Midpoint: (1.5, 2.0).
# 2) Border: A=(2, 2), B=(2, 2) -> Distance: 0.0.
# 3) Error: x1="hello" -> Error: invalid input.
# ------------------------------------------------------------

print("\\n=== Problem 2: Points and Distances ===")
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)
except ValueError:
    print("Error: invalid input")

# ============================================================
# CONCLUSIONS
# Lists are useful when a collection needs to change as the program runs.
# Their append(), insert(), remove(), and pop() methods support common updates.
# Tuples are useful for fixed records, such as points with x and y coordinates.
# A tuple cannot be changed after it has been created.
# Dictionaries connect keys with values and make lookups by key straightforward.
# Combining dictionaries and lists is useful for grouped information, such as grades.
# Input validation helps prevent invalid values from causing incorrect results.
# Clear names and messages make a program easier to understand and test.

# REFERENCES
# 1) Python Software Foundation. Built-in Types:
#    https://docs.python.org/3/library/stdtypes.html
# 2) Python Software Foundation. Data Structures:
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Python Software Foundation. Built-in Functions:
#    https://docs.python.org/3/library/functions.html
# 4) Python Software Foundation. Errors and Exceptions:
#    https://docs.python.org/3/tutorial/errors.html
# 5) Python Software Foundation. An Informal Introduction to Python:
#    https://docs.python.org/3/tutorial/introduction.html
# 6) Python Software Foundation. More on Lists:
#    https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# ============================================================