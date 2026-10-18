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


# ------------------------------------------------------------
# Problem 3: Product catalog with dictionary
#
# Description:
# Use a dictionary to store product names and unit prices.
# Find a requested product and calculate the cost for the requested quantity.
#
# Inputs:
# - Product name.
# - Quantity to buy as an integer.
#
# Outputs:
# - Unit price, quantity, and total price, or an error message.
#
# Validations:
# - Product name must not be empty and must exist in the catalog.
# - Quantity must be an integer greater than zero.
#
# Test cases:
# 1) Normal: product="apple", quantity=3 -> Unit price: 10.0; Total: 30.0.
# 2) Border: product="bread", quantity=1 -> Total: 25.0.
# 3) Error: product="tablet" or quantity=0 -> Error message.
# ------------------------------------------------------------

print("\\n=== Problem 3: Product Catalog ===")
product_prices = {
    "apple": 10.0,
    "bread": 25.0,
    "milk": 32.5
}

product_name = input("Enter a product name (apple, bread, milk): ").strip().lower()
quantity_text = input("Enter quantity: ")

try:
    quantity = int(quantity_text)

    if product_name == "" or quantity <= 0:
        print("Error: invalid input")
    elif product_name not in product_prices:
        print("Error: product not found")
    else:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", round(total_price, 2))
except ValueError:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 4: Student grades with dict and list
#
# Description:
# Store each student's grades in a dictionary of lists.
# Calculate the selected student's average and determine whether they passed.
#
# Inputs:
# - Student name.
#
# Outputs:
# - Grades, average, and Passed (True or False), or an error message.
#
# Validations:
# - Student name must not be empty and must exist in the dictionary.
# - Check that the grade list is not empty before calculating the average.
#
# Test cases:
# 1) Normal: "Alice" -> Grades: [90.0, 85.0, 95.0]; Passed: True.
# 2) Border: "Charlie" -> Grades: [60.0, 70.0]; Average: 65.0; Passed: False.
# 3) Error: "Morgan" -> Error: student not found.
# ------------------------------------------------------------

print("\\n=== Problem 4: Student Grades ===")
student_grades = {
    "Alice": [90.0, 85.0, 95.0],
    "Bob": [72.0, 68.0, 80.0],
    "Charlie": [60.0, 70.0]
}

student_name = input("Enter a student name (Alice, Bob, Charlie): ").strip().title()

if student_name == "":
    print("Error: invalid input")
elif student_name not in student_grades:
    print("Error: student not found")
else:
    grades_list = student_grades[student_name]
    if len(grades_list) == 0:
        print("Error: no grades available")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0
        print("Grades:", grades_list)
        print("Average:", round(average, 2))
        print("Passed:", is_passed)


# ------------------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
#
# Description:
# Convert a sentence to lowercase, make a list of words, and count how often
# each word appears. Display the frequency dictionary and most common word.
#
# Inputs:
# - A sentence.
#
# Outputs:
# - Words list, frequency dictionary, and most common word.
#
# Validations:
# - The sentence must not be empty.
# - Basic punctuation (, . ! ?) is replaced with spaces.
# - Check that the resulting word list is not empty.
#
# Test cases:
# 1) Normal: "cat dog cat" -> cat: 2, dog: 1; Most common word: cat.
# 2) Border: "hello" -> one word; frequency is 1.
# 3) Error: empty sentence -> Error: invalid input.
# ------------------------------------------------------------

print("\\n=== Problem 5: Word Frequency Counter ===")
sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    clean_sentence = sentence.lower()
    clean_sentence = clean_sentence.replace(",", " ")
    clean_sentence = clean_sentence.replace(".", " ")
    clean_sentence = clean_sentence.replace("!", " ")
    clean_sentence = clean_sentence.replace("?", " ")
    words_list = clean_sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] = freq_dict[word] + 1
            else:
                freq_dict[word] = 1

        most_common_word = words_list[0]
        highest_frequency = freq_dict[most_common_word]

        for word in freq_dict:
            if freq_dict[word] > highest_frequency:
                most_common_word = word
                highest_frequency = freq_dict[word]

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# ------------------------------------------------------------
# Problem 6: Simple contact book (dictionary CRUD)
#
# Description:
# Use a dictionary to add, search, or delete a contact.
# Contact names are keys and phone numbers are string values.
#
# Inputs:
# - Action: ADD, SEARCH, or DELETE.
# - Contact name.
# - Phone number, only for ADD.
#
# Outputs:
# - A success message or a clear error message.
#
# Validations:
# - Action is normalized to uppercase and must be valid.
# - Name must not be empty.
# - Phone must not be empty when adding a contact.
# - Check whether a contact exists before searching or deleting.
#
# Test cases:
# 1) Normal: action="ADD", name="Sam", phone="5551234" -> Contact saved.
# 2) Border: SEARCH for a name that does not exist -> Error: contact not found.
# 3) Error: action="UPDATE" -> Error: invalid action.
# ------------------------------------------------------------

print("\\n=== Problem 6: Simple Contact Book ===")
contacts = {
    "Alice": "1112223333",
    "Bob": "4445556666",
    "Charlie": "7778889999"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    name = input("Enter contact name: ").strip().title()

    if name == "":
        print("Error: invalid input")
    elif action_text == "ADD":
        phone = input("Enter phone number: ").strip()

        if phone == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts.get(name))
        else:
            print("Error: contact not found")
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")


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