# ---------------------------------------------------------------
# PORTADA
# ---------------------------------------------------------------
# Student: Oskar Alvarez Najera
# Student ID: 2630002
# Group: t_strings
# Course: Algorithms and Programming
# Topic: Strings in Python
#
# ---------------------------------------------------------------
# RESUMEN EJECUTIVO
# ---------------------------------------------------------------
# A string in Python is an immutable sequence of Unicode characters,
# meaning that once it is created it cannot be modified in place; any
# operation that changes it returns a NEW string. Common operations
# include concatenation (+), repetition (*), computing its length
# with len(), extracting sub-strings via slicing (text[a:b]), searching
# with find() / in, and replacing text with replace().
# Validating and normalizing user input (emails, names, passwords) is
# essential to avoid errors and to compare data consistently: using
# strip() and lower() before comparing is a good practice. This
# document contains six problems that practice creation, indexing,
# slicing, concatenation, search, replacement, split, join, formatting,
# and validation of strings, each one with description, inputs,
# outputs, validations and three test cases (normal, border, error).
#
# ---------------------------------------------------------------
# GOOD PRACTICES APPLIED
# ---------------------------------------------------------------
# - Strings are immutable: every transformation creates a new string.
# - Normalize input with strip() and lower() before comparing.
# - Avoid magic numbers in indices; document what each slice extracts.
# - Prefer string methods over rewriting basic logic.
# - Design validations in order: non-empty first, then format.
# - Write readable code: clear variable names and clear error messages.
#
# =============================================================================


# =============================================================================
# Problem 1: Full name formatter (name + initials)
# -----------------------------------------------------------------------------
# Description: Reads a full name in a single string, normalizes spaces and
#   capitalization, prints it in Title Case and shows the initials with dots.
#
# Inputs:
# - full_name (str): may come in any case, with extra spaces.
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - full_name must not be empty after strip().
# - Must contain at least two words.
#
# Test cases:
# 1) Normal: "juan carlos tovar"  -> Formatted: "Juan Carlos Tovar" | Initials: J.C.T.
# 2) Border: "  ana   maria  lopez " -> "Ana Maria Lopez" | A.M.L.
# 3) Error : "   " -> "Error: invalid input"
# =============================================================================

def problem_1_full_name_formatter():
    print("\n--- Problem 1: Full name formatter ---")
    full_name = input("Enter full name: ").strip()

    # Validation 1: non-empty after strip
    if full_name == "":
        print("Error: invalid input")
        return

    # Normalize extra spaces by splitting and joining
    words = full_name.split()

    # Validation 2: at least two words
    if len(words) < 2:
        print("Error: invalid input")
        return

    # Title case formatted name
    formatted_name = " ".join(word.capitalize() for word in words)

    # Build initials with dots: X.X.X.
    initials = ""
    for word in words:
        initials += word[0].upper() + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# =============================================================================
# Problem 2: Simple email validator (structure + domain)
# -----------------------------------------------------------------------------
# Description: Validates a basic email format: exactly one '@', at least one
#   '.' after the '@', and no whitespace. Shows the domain if valid.
#
# Inputs:
# - email_text (str)
#
# Outputs:
# - "Valid email: true" / "Valid email: false"
# - "Domain: <domain_part>" when valid.
#
# Validations:
# - email_text not empty after strip().
# - Exactly one '@'.
# - No spaces.
# - At least one '.' after the '@'.
#
# Test cases:
# 1) Normal: "user@example.com"  -> Valid: true  | Domain: example.com
# 2) Border: "a@b.co"            -> Valid: true  | Domain: b.co
# 3) Error : "user.example.com"  -> Valid: false
# =============================================================================

def problem_2_email_validator():
    print("\n--- Problem 2: Simple email validator ---")
    email_text = input("Enter email: ").strip()

    # Validation: non-empty
    if email_text == "":
        print("Error: invalid input")
        return

    # Validation: exactly one '@'
    if email_text.count("@") != 1:
        print("Valid email: false")
        return

    # Validation: no whitespace
    if " " in email_text:
        print("Valid email: false")
        return

    at_index = email_text.find("@")
    local_part = email_text[:at_index]        # text before '@'
    domain_part = email_text[at_index + 1:]   # text after '@'

    # Validation: local part and domain non-empty, dot in domain
    if local_part == "" or domain_part == "" or "." not in domain_part:
        print("Valid email: false")
        return

    print("Valid email: true")
    print(f"Domain: {domain_part}")


# =============================================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# -----------------------------------------------------------------------------
# Description: Determines if a phrase is a palindrome, ignoring spaces and
#   capitalization. It also shows the normalized version.
#
# Inputs:
# - phrase (str)
#
# Outputs:
# - "Normalized: <clean_text>"
# - "Is palindrome: true" / "Is palindrome: false"
#
# Validations:
# - phrase not empty after strip().
# - At least 3 characters after removing spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> Normalized: "anitalavalatina" -> true
# 2) Border: "aba"                -> true
# 3) Error : ""                   -> "Error: invalid input"
# =============================================================================

def problem_3_palindrome_checker():
    print("\n--- Problem 3: Palindrome checker ---")
    phrase = input("Enter a phrase: ").strip()

    # Validation: non-empty
    if phrase == "":
        print("Error: invalid input")
        return

    # Normalize: lower case and remove spaces
    clean_text = phrase.lower().replace(" ", "")

    # Validation: minimum reasonable length
    if len(clean_text) < 3:
        print("Error: invalid input")
        return

    reversed_text = clean_text[::-1]  # reverse using slicing

    print(f"Normalized: {clean_text}")
    if clean_text == reversed_text:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")


# =============================================================================
# Problem 4: Sentence word stats (lengths and first/last word)
# -----------------------------------------------------------------------------
# Description: Splits a sentence into words and reports total count,
#   first word, last word, shortest word and longest word.
#
# Inputs:
# - sentence (str)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - Sentence not empty after strip().
# - Must have at least one word after split().
#
# Test cases:
# 1) Normal: "Python is a great language" -> count 5, first "Python",
#    last "language", shortest "a", longest "language"
# 2) Border: "Hello"                      -> count 1, first=last="Hello"
# 3) Error : "    "                       -> "Error: invalid input"
# =============================================================================

def problem_4_sentence_word_stats():
    print("\n--- Problem 4: Sentence word stats ---")
    sentence = input("Enter a sentence: ").strip()

    # Validation: non-empty
    if sentence == "":
        print("Error: invalid input")
        return

    words = sentence.split()

    # Validation: at least one word
    if len(words) == 0:
        print("Error: invalid input")
        return

    first_word = words[0]
    last_word = words[-1]

    shortest_word = words[0]
    longest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Word count: {len(words)}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# =============================================================================
# Problem 5: Password strength classifier
# -----------------------------------------------------------------------------
# Description: Classifies a password as weak, medium or strong according to
#   length and the presence of upper, lower, digit and symbol characters.
#
# Rules:
# - weak   : length < 8 OR all characters are the same type.
# - medium : length >= 8 and at least two character types.
# - strong : length >= 8 and contains upper, lower, digit and symbol.
#
# Inputs:
# - password_input (str)
#
# Outputs:
# - "Password strength: weak|medium|strong"
#
# Validations:
# - Password must not be empty.
#
# Test cases:
# 1) Normal: "Abcdef1!"   -> strong
# 2) Border: "abcdefgh"   -> weak (only lowercase)
# 3) Error : ""           -> "Error: invalid input"
# =============================================================================

def problem_5_password_strength():
    print("\n--- Problem 5: Password strength classifier ---")
    password_input = input("Enter password: ")

    # Validation: non-empty (do not strip passwords here, but reject empty)
    if password_input.strip() == "":
        print("Error: invalid input")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    # Count how many types are present
    type_count = 0
    if has_upper: type_count += 1
    if has_lower: type_count += 1
    if has_digit: type_count += 1
    if has_symbol: type_count += 1

    length = len(password_input)

    if length < 8 or type_count == 1:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")


# =============================================================================
# Problem 6: Product label formatter (fixed-width text)
# -----------------------------------------------------------------------------
# Description: Builds a fixed-width label of exactly 30 characters using the
#   product name and price. Short labels are padded with spaces; long labels
#   are truncated to 30 characters.
#
# Inputs:
# - product_name (str)
# - price_value  (str or number, must convert to positive float)
#
# Outputs:
# - 'Label: "<exactly 30 characters>"'
#
# Validations:
# - product_name not empty after strip().
# - price_value must be a positive number.
#
# Test cases:
# 1) Normal: "Laptop", "999.99"    -> padded to 30 chars
# 2) Border: "A"*40, "1"           -> truncated to 30 chars
# 3) Error : "  ", "abc"           -> "Error: invalid input"
# =============================================================================

def problem_6_product_label():
    print("\n--- Problem 6: Product label formatter ---")
    product_name = input("Enter product name: ").strip()
    price_raw = input("Enter price: ").strip()

    # Validation: product name non-empty
    if product_name == "":
        print("Error: invalid input")
        return

    # Validation: price must be a positive number
    try:
        price_value = float(price_raw)
    except ValueError:
        print("Error: invalid input")
        return

    if price_value <= 0:
        print("Error: invalid input")
        return

    # Format price with two decimals
    price_text = f"{price_value:.2f}"

    # Build base label
    base_label = f"Product: {product_name} | Price: ${price_text}"

    # Pad with spaces or truncate to exactly 30 characters
    if len(base_label) < 30:
        label = base_label + " " * (30 - len(base_label))
    else:
        label = base_label[:30]

    print(f'Label: "{label}"')


# =============================================================================
# MAIN
# =============================================================================
def main():
    problem_1_full_name_formatter()
    problem_2_email_validator()
    problem_3_palindrome_checker()
    problem_4_sentence_word_stats()
    problem_5_password_strength()
    problem_6_product_label()


if __name__ == "__main__":
    main()


# =============================================================================
# CONCLUSIONES
# =============================================================================
# String handling is essential in nearly every program because almost all
# input and output flows through text. Methods such as lower() and strip()
# should be used before comparing data, while split() and join() help to
# manipulate words efficiently without manual loops. Normalizing text
# guarantees consistent comparisons and avoids false negatives. Designing
# validations step by step (non-empty, format, semantic rules) prevents
# garbage data and runtime errors. Working through these problems made it
# clear that strings are immutable: each operation returns a new object,
# and slicing (including text[::-1]) is a powerful and safe way to extract
# or reverse content.
#
# =============================================================================
# REFERENCES
# =============================================================================
# 1) Python documentation - Built-in Types: Text Sequence Type — str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - String Methods
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) W3Schools - Python Strings Tutorial
#    https://www.w3schools.com/python/python_strings.asp
# 4) Real Python - Python String Formatting Best Practices
#    https://realpython.com/python-string-formatting/
# 5) Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media.
# 6) Downey, A. (2015). Think Python: How to Think Like a Computer Scientist.
# =============================================================================