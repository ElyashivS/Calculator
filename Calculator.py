"""
    Program: Magical Calculator
    Author: Elyashiv via Udemy course
"""


import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def perform_math():
    global run
    global previous

    # If there has been a previous calculation, use that result as a prompt
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    # If user quit ->
    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
