# ============================================================
# Student: Oskar Tadeo Alvarez Najera
# Student ID: 2630002
# Group: IM 1-1
# Subject: Python Strings
# ============================================================

# EXECUTIVE SUMMARY
#   A string is a Python data type used to store text, such as names,
#   sentences, email addresses, passwords, and product labels.
#   Strings are immutable, which means that their characters cannot be
#   changed directly; string operations create new strings instead.
#   Common operations include joining text, measuring its length,
#   extracting slices, searching for text, and replacing characters.
#   Input validation helps prevent empty, incorrectly formatted, or
#   unexpected data from being processed as if it were valid.
#   Normalization, such as removing extra spaces and using lowercase,
#   makes text comparisons more consistent and reliable.
#   This file contains six problems with descriptions, inputs, outputs,
#   validations, example test cases, and Python code for each solution.

# PRINCIPLES AND GOOD PRACTICES
#   - Strings are immutable: operations create a new string.
#   - Use strip() and lower() to normalize text before comparisons.
#   - Explain slice indexes instead of using unexplained numbers.
#   - Prefer built-in string methods over unnecessarily complex logic.
#   - Validate in a clear order: check for empty input, then its format.
#   - Use readable variable names and understandable error messages.
#   - The examples use introductory concepts such as input(), print(),
#     if/elif/else, for loops, lists, indexing, slicing, and f-strings.
#   - Some string methods are included because they are required by this
#     assignment: strip(), split(), replace(), count(), find(), and others.


# ============================================================
# PROBLEM 1: FULL NAME FORMATTER
# Description:
# Normalize a full name, display it in title case, and create initials.
# Extra spaces around the name are removed and repeated spaces are
# handled by split() followed by join().
#
# Inputs:
# - full_name: a person's full name.
#
# Outputs:
# - Formatted name and initials.
#
# Validations:
# - The name cannot be empty after removing surrounding spaces.
# - At least two words are required.
#
# Test cases:
# 1) Normal: "  juan   carlos tovar " -> "Juan Carlos Tovar", "J.C.T."
# 2) Border: "ana lopez" -> "Ana Lopez", "A.L."
# 3) Error: "     " -> "Error: name cannot be empty"
# ============================================================

print("\n=== Problem 1: Full Name Formatter ===")
full_name = input("Enter your full name: ")
full_name = full_name.strip()

if full_name == "":
    print("Error: name cannot be empty")
else:
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Error: enter at least two words")
    else:
        clean_name = " ".join(name_parts).title()
        initials = ""
        for name_part in name_parts:
            initials = initials + name_part[0].upper() + "."
        print(f"Formatted name: {clean_name}")
        print(f"Initials: {initials}")


# ============================================================
# PROBLEM 2: SIMPLE EMAIL VALIDATOR
# Description:
# Check a basic email structure and display its domain when valid.
# This is a simple classroom check, not a complete email standard
# validator.
#
# Inputs:
# - email_text: an email address.
#
# Outputs:
# - "Valid email: true" or "Valid email: false".
# - The domain when the email is valid.
#
# Validations:
# - The input cannot be empty.
# - It must contain exactly one '@'.
# - It cannot contain spaces.
# - There must be text before '@' and a dot after '@'.
#
# Test cases:
# 1) Normal: "student@example.com" -> valid, domain "example.com"
# 2) Border: "a@b.c" -> valid under these simple rules
# 3) Error: "studentexample.com" -> invalid because '@' is missing
# ============================================================

print("\n=== Problem 2: Simple Email Validator ===")
email_text = input("Enter an email address: ")
email_text = email_text.strip()

if email_text == "":
    print("Error: email cannot be empty")
    print("Valid email: false")
elif email_text.count("@") != 1:
    print("Valid email: false")
elif " " in email_text:
    print("Valid email: false")
else:
    at_position = email_text.find("@")
    domain_part = email_text[at_position + 1:]
    name_part = email_text[:at_position]

    if name_part == "" or "." not in domain_part:
        print("Valid email: false")
    elif domain_part.startswith(".") or domain_part.endswith("."):
        print("Valid email: false")
    else:
        print("Valid email: true")
        print(f"Domain: {domain_part}")


# ============================================================
# PROBLEM 3: PALINDROME CHECKER
# Description:
# Determine whether a phrase reads the same forward and backward.
# The comparison ignores spaces and letter case.
#
# Inputs:
# - phrase: a phrase to check.
#
# Outputs:
# - The normalized phrase and whether it is a palindrome.
#
# Validations:
# - The phrase cannot be empty.
# - At least three non-space characters are required.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> true
# 2) Border: "aba" -> true
# 3) Error: " a " -> error because only one character remains
# ============================================================

print("\n=== Problem 3: Palindrome Checker ===")
phrase = input("Enter a phrase: ")
phrase = phrase.strip()

if phrase == "":
    print("Error: phrase cannot be empty")
else:
    normalized_phrase = phrase.lower().replace(" ", "")
    if len(normalized_phrase) < 3:
        print("Error: enter at least three non-space characters")
    else:
        reversed_phrase = normalized_phrase[::-1]
        print(f"Normalized phrase: {normalized_phrase}")
        if normalized_phrase == reversed_phrase:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")


# ============================================================
# PROBLEM 4: SENTENCE WORD STATS
# Description:
# Count the words in a sentence and show the first, last, shortest,
# and longest word. If words tie in length, the first matching word
# is kept.
#
# Inputs:
# - sentence: a sentence.
#
# Outputs:
# - Word count, first word, last word, shortest word, longest word.
#
# Validations:
# - The sentence cannot be empty after strip().
# - At least one word must remain after split().
#
# Test cases:
# 1) Normal: "Python makes learning fun" -> 4 words; shortest "fun"
# 2) Border: "hello" -> 1 word; first and last are "hello"
# 3) Error: "   " -> error because the sentence is empty
# ============================================================

print("\n=== Problem 4: Sentence Word Stats ===")
sentence = input("Enter a sentence: ")
sentence = sentence.strip()

if sentence == "":
    print("Error: sentence cannot be empty")
else:
    words = sentence.split()
    if len(words) == 0:
        print("Error: enter at least one word")
    else:
        shortest_word = words[0]
        longest_word = words[0]

        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word
            if len(word) > len(longest_word):
                longest_word = word

        print(f"Word count: {len(words)}")
        print(f"First word: {words[0]}")
        print(f"Last word: {words[len(words) - 1]}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")


# ============================================================
# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
# Description:
# Classify a password as weak, medium, or strong using simple rules.
# Strong requires at least 8 characters, uppercase and lowercase
# letters, a digit, and a symbol. Medium requires at least 8
# characters and at least two of those character categories.
#
# Inputs:
# - password_input: the password to classify.
#
# Outputs:
# - Password strength: weak, medium, or strong.
#
# Validations:
# - The password cannot be empty.
# - Length is checked before assigning a strength.
#
# Test cases:
# 1) Normal: "Hello123!" -> strong
# 2) Border: "hello123" -> medium
# 3) Error: "" -> error because the password is empty
# ============================================================

print("\n=== Problem 5: Password Strength Classifier ===")
password_input = input("Enter a password: ")

if password_input == "":
    print("Error: password cannot be empty")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        else:
            has_symbol = True

    category_count = 0
    if has_upper:
        category_count = category_count + 1
    if has_lower:
        category_count = category_count + 1
    if has_digit:
        category_count = category_count + 1
    if has_symbol:
        category_count = category_count + 1

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif category_count >= 2:
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")


# ============================================================
# PROBLEM 6: PRODUCT LABEL FORMATTER
# Description:
# Create a product label in the format
# "Product: NAME | Price: $PRICE" and make it exactly 30 characters.
# Labels longer than 30 characters are cut off; shorter labels are
# padded with spaces at the end.
#
# Inputs:
# - product_name: product name.
# - price_value: a positive numeric price.
#
# Outputs:
# - The label surrounded by quotes and its length.
#
# Validations:
# - The product name cannot be empty.
# - Price must be numeric and greater than zero.
#
# Test cases:
# 1) Normal: name "Pen", price "2.5" -> a 30-character label
# 2) Border: name "A", price "1" -> padded to 30 characters
# 3) Error: name "Pen", price "abc" -> invalid price
# ============================================================

print("\n=== Problem 6: Product Label Formatter ===")
product_name = input("Enter the product name: ").strip()
price_text = input("Enter the positive price: ").strip()

if product_name == "":
    print("Error: product name cannot be empty")
else:
    # Validate a simple positive integer or decimal price.
    # This loop accepts digits and at most one decimal point.
    price_format_is_valid = price_text != ""
    decimal_point_count = 0
    digit_count = 0

    for character in price_text:
        if character.isdigit():
            digit_count = digit_count + 1
        elif character == ".":
            decimal_point_count = decimal_point_count + 1
        else:
            price_format_is_valid = False

    if decimal_point_count > 1 or digit_count == 0:
        price_format_is_valid = False

    if price_format_is_valid:
        try:
            price_number = float(price_text)
        except ValueError:
            price_format_is_valid = False

    if not price_format_is_valid:
        print("Error: price must be a positive number")
    elif price_number <= 0:
        print("Error: price must be greater than zero")
    else:
        label = f"Product: {product_name} | Price: ${price_text}"

        if len(label) > 30:
            label = label[:30]
        elif len(label) < 30:
            label = label + (" " * (30 - len(label)))

        print(f'Label: "{label}"')
        print(f"Label length: {len(label)}")


# ============================================================
# CONCLUSIONS
# - Strings are essential for reading, processing, and displaying data.
# - lower() helps compare text without case differences.
# - strip() removes surrounding whitespace, while split() separates
#   text into words and join() combines words into one string.
# - Normalizing input before comparing it makes results more reliable.
# - Clear validations prevent empty or incorrectly formatted data
#   from being processed as valid input.
# - Strings are immutable, so methods such as replace() return new text.
# - Slicing is useful for extracting parts of text or limiting its size.
# - Testing normal, border, and error cases helps reveal mistakes.

# REFERENCES
# 1) Python Software Foundation. Built-in Types: Text Sequence Type — str.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python Software Foundation. Built-in Functions.
#    https://docs.python.org/3/library/functions.html
# 3) Python Software Foundation. An Informal Introduction to Python.
#    https://docs.python.org/3/tutorial/introduction.html
# 4) Python Software Foundation. More on Strings.
#    https://docs.python.org/3/tutorial/introduction.html#strings
# 5) Python Software Foundation. Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
# 6) Python Software Foundation. Input and Output.
#    https://docs.python.org/3/tutorial/inputoutput.html
