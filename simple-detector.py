'''
🎯 Case Study: Simple Access Detector
📝 Case Description:
    1. You're building a simple security system. There are two conditions that determine whether a person is allowed to enter:
    2. They have an access card (has_card) – True or False.
    3. They have the correct PIN (has_pin) – True or False.

However, there's also a security override code represented as a 4-bit binary number (e.g., 0b0100).

📌 Access Rules:
A person is allowed to enter if:
    1. They have both an access card and the correct PIN,
    2. Or the override code indicates emergency access (i.e., the 3rd bit from the right is 1, for example: 0b0100).

📌 Your Task:
Create 3 variables:
    1. has_card (Boolean)
    2. has_pin (Boolean)
    3. override_code (Integer in binary format, e.g., 0b0100)

Use logical and bitwise operators to determine whether the person is allowed access.
Display the result using print().

This is a simple case example to apply learning from logical and bitwise operations.
'''

has_card = True
has_pin = True
override_code = 0b0100

Allowaccess = bool((has_card and has_pin) or (override_code & 0b0100))
print("Can i login?: ", Allowaccess)
DeniedAccess = not Allowaccess
print("Can i login?: ", DeniedAccess)