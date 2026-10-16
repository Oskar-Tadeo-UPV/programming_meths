# ============================================================
# Student: Oskar Tadeo Alvarez Najera
# Student ID: 2630002
# Group: IM 1-1
# Subject: Python Strings
# ============================================================

# EXECUTIVE SUMMARY
# ============================================================
# Python uses int to represent whole numbers, such as age or hours.
# The float type represents numbers that can contain decimal places.
# Boolean values are True and False and represent logical conditions.
# Comparisons such as >=, <, and == produce boolean values.
# Logical operators such as and, or, and not combine or reverse conditions.
# Validating input helps prevent invalid calculations and unexpected results.
# Checking ranges is important, and division by zero must be avoided.
# This file contains six problems using numeric types, casting, rounding,
# arithmetic, comparisons, boolean expressions, and simple decisions.
# Each problem documents its inputs, outputs, validations, and test cases.
#
# ============================================================

# ============================================================
# PROBLEM 1: TEMPERATURE CONVERTER AND RANGE FLAG
# ============================================================
# Description:
# Convert a temperature from Celsius to Fahrenheit and Kelvin.
# Also determine whether the temperature is high (30 degrees Celsius or more).
#
# Inputs:
# - temp_c: temperature in Celsius, as a float.
#
# Outputs:
# - Fahrenheit, Kelvin, and High temperature (true/false).
#
# Validations:
# - The input must be convertible to float.
# - Kelvin must be at least 0.0, so Celsius cannot be below -273.15.
#
# Test cases:
# 1) Normal: temp_c = 30 -> Fahrenheit = 86.0, Kelvin = 303.15, high = true.
# 2) Border: temp_c = -273.15 -> Kelvin = 0.0, high = false.
# 3) Error: temp_c = "cold" -> display "Error: invalid input".
# ============================================================

print("\n=== Problem 1: Temperature Converter ===")
try:
    temp_c = float(input("Enter temperature in Celsius: "))

    if temp_c < -273.15:
        print("Error: invalid input")
        print("Temperature cannot be below absolute zero.")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit: {round(temp_f, 2)}")
        print(f"Kelvin: {round(temp_k, 2)}")
        print(f"High temperature: {str(is_high_temperature).lower()}")
except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 2: WORK HOURS AND OVERTIME PAYMENT
# ============================================================
# Description:
# Calculate weekly pay using the normal hourly rate for up to 40 hours.
# Hours above 40 are paid at 150% of the normal hourly rate.
#
# Inputs:
# - hours_worked: number of hours worked, as a float.
# - hourly_rate: hourly pay rate, as a float.
#
# Outputs:
# - Regular pay, overtime pay, total pay, and Has overtime (true/false).
#
# Validations:
# - hours_worked must be >= 0.
# - hourly_rate must be > 0.
# - Both values must be convertible to float.
#
# Test cases:
# 1) Normal: 45 hours at 100 -> regular = 4000, overtime = 750, total = 4750.
# 2) Border: 40 hours at 100 -> regular = 4000, overtime = 0, total = 4000.
# 3) Error: hours_worked = -2 -> display "Error: invalid input".
# ============================================================

print("\n=== Problem 2: Work Hours and Overtime ===")
try:
    hours_worked = float(input("Enter hours worked this week: "))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40.0

        print(f"Regular pay: {round(regular_pay, 2)}")
        print(f"Overtime pay: {round(overtime_pay, 2)}")
        print(f"Total pay: {round(total_pay, 2)}")
        print(f"Has overtime: {str(has_overtime).lower()}")
except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 3: DISCOUNT ELIGIBILITY WITH BOOLEANS
# ============================================================
# Description:
# A customer receives a 10% discount if they are a student, are a senior,
# or have a purchase total of at least 1000.00.
#
# Inputs:
# - purchase_total: purchase amount, as a float.
# - is_student_text: YES or NO.
# - is_senior_text: YES or NO.
#
# Outputs:
# - Discount eligible (true/false) and Final total.
#
# Validations:
# - purchase_total must be >= 0.
# - Student and senior answers are normalized to uppercase.
# - Answers must be YES or NO.
#
# Test cases:
# 1) Normal: total = 500, student = YES, senior = NO -> eligible = true, total = 450.
# 2) Border: total = 1000, student = NO, senior = NO -> eligible = true, total = 900.
# 3) Error: student answer = MAYBE -> display "Error: invalid input".
# ============================================================

print("\n=== Problem 3: Discount Eligibility ===")
try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Is the customer a student? (YES/NO): ").upper().lstrip().rstrip()
    is_senior_text = input("Is the customer a senior? (YES/NO): ").upper().lstrip().rstrip()

    if purchase_total < 0:
        print("Error: invalid input")
    elif (is_student_text != "YES" and is_student_text != "NO") or (is_senior_text != "YES" and is_senior_text != "NO"):
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"
        discount_eligible = is_student or is_senior or purchase_total >= 1000.0

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {round(final_total, 2)}")
except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 4: BASIC STATISTICS OF THREE INTEGERS
# ============================================================
# Description:
# Read three integers and calculate their sum, average, maximum, and minimum.
# Determine whether all three numbers are even.
#
# Inputs:
# - n1, n2, n3: integer values.
#
# Outputs:
# - Sum, Average, Max, Min, and All even (true/false).
#
# Validations:
# - Each input must be convertible to int.
# - Negative integers are allowed.
#
# Test cases:
# 1) Normal: 2, 4, 6 -> sum = 12, average = 4.0, all even = true.
# 2) Border: 0, 0, 0 -> sum = 0, average = 0.0, all even = true.
# 3) Error: n2 = "four" -> display "Error: invalid input".
# ============================================================

print("\n=== Problem 4: Basic Statistics ===")
try:
    n1 = int(input("Enter the first integer: "))
    n2 = int(input("Enter the second integer: "))
    n3 = int(input("Enter the third integer: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")
except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 5: LOAN ELIGIBILITY (INCOME AND DEBT RATIO)
# ============================================================
# Description:
# Determine loan eligibility based on monthly income, monthly debt, and
# credit score. Eligibility requires income >= 8000, debt ratio <= 0.4,
# and credit score >= 650.
#
# Inputs:
# - monthly_income: monthly income, as a float.
# - monthly_debt: monthly debt payments, as a float.
# - credit_score: credit score, as an integer.
#
# Outputs:
# - Debt ratio and Eligible (true/false).
#
# Validations:
# - monthly_income must be > 0 to prevent division by zero.
# - monthly_debt and credit_score must be >= 0.
# - Inputs must convert to their required numeric types.
#
# Test cases:
# 1) Normal: income = 10000, debt = 3000, score = 700 -> ratio = 0.3, eligible = true.
# 2) Border: income = 8000, debt = 3200, score = 650 -> ratio = 0.4, eligible = true.
# 3) Error: income = 0 -> display "Error: invalid input".
# ============================================================

print("\n=== Problem 5: Loan Eligibility ===")
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt payments: "))
    credit_score = int(input("Enter credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)

        print(f"Debt ratio: {round(debt_ratio, 2)}")
        print(f"Eligible: {str(eligible).lower()}")
except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 6: BODY MASS INDEX (BMI) AND CATEGORY FLAG
# ============================================================
# Description:
# Calculate BMI using weight in kilograms and height in meters.
# Display the BMI rounded to two decimal places and the requested category flags.
#
# Inputs:
# - weight_kg: weight in kilograms, as a float.
# - height_m: height in meters, as a float.
#
# Outputs:
# - BMI, Underweight, Normal, and Overweight (true/false).
#
# Validations:
# - weight_kg must be > 0.
# - height_m must be > 0 to prevent division by zero.
# - Both inputs must be convertible to float.
#
# Test cases:
# 1) Normal: weight = 68, height = 1.70 -> BMI = 23.53, normal = true.
# 2) Border: weight = 50, height = 1.70 -> BMI = 17.30, underweight = true.
# 3) Error: height = 0 -> display "Error: invalid input".
#
# Educational note: BMI categories are simplified mathematical ranges and
# are not, by themselves, a medical assessment.
# ============================================================

print("\n=== Problem 6: Body Mass Index (BMI) ===")
try:
    weight_kg = float(input("Enter weight in kilograms: "))
    height_m = float(input("Enter height in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = (bmi >= 18.5) and (bmi < 25.0)
        is_overweight = bmi >= 25.0

        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")
except ValueError:
    print("Error: invalid input")


# ============================================================
# CONCLUSIONS
# ============================================================
# Integers are useful for whole-number values, while floats support decimal
# values needed for measurements, money, averages, and ratios.
# Comparisons create boolean values that can be used by if statements.
# Validating input and ranges prevents many invalid calculations.
# Checking divisors before division prevents division-by-zero errors.
# The and, or, and not operators help combine conditions into clear rules.
# These techniques can be applied to payroll, discounts, loans, and statistics.
# Clear names, intermediate variables, and helpful error messages make programs
# easier to understand, test, and maintain.
#
# ============================================================
# REFERENCES
# ============================================================
# 1) Python Software Foundation. Built-in Types: Numeric Types.
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python Software Foundation. Boolean Type - bool.
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python Software Foundation. Built-in Functions (int, float, min, max, round).
#    https://docs.python.org/3/library/functions.html
# 4) Python Software Foundation. Expressions: Comparisons and Boolean Operations.
#    https://docs.python.org/3/reference/expressions.html
# 5) Python Software Foundation. Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
# 6) Python Software Foundation. An Informal Introduction to Python.
#    https://docs.python.org/3/tutorial/introduction.html
# ============================================================