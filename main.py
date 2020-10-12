# This is the first calculator made in Python ever! Hope you like it! ps: Don't solve big problems :(


# Reading the numeric expression from the console
def read_expression():
    print("Hello, I'm your new calculator, write your expression under this line:")
    expression = input()
    return expression


# Printing the result of the expression
def result_of_expression():
    result = eval(read_expression())
    print("the result of you expression is: ", result)
    return result


result_of_expression()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
