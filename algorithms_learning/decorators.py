# this file for only learning python decorators and

# simple function in python
# def plus_one(number):
#     return number + 1


"""Siple function inside an another functino and calling it"""
# def plus_one(number):
#     def add_num(number):
#         return number + 1
#     result = add_num(number)
#     return result

"""Sending function as a argument to another functino !"""

# def add_num(num1, num2):
#     return num1 + num2

# def split_num(num1, num2):
#     return num1 + num2

# def multiply_num(num1, num2):
#     return num1 + num2

# def divide_num(num1, num2):
#     return num1 + num2


# def do_math(function, num1, num2):
#     return function(num1, num2)

""" Function that returns another functions """

# def do_math():
#     def add_num():
#         return "Hello decorators!"

#     return add_num

""" 
Nested Functions have access to the 
Enclosing Function's Variable Scope
Python allows a nested function to 
access the outer scope of the enclosing
function. This is a critical concept 
in decorators -- this pattern is known 
as a Closur 
"""

# def print_mine(message):
#     def message_printer():
#         print(message)

#     message_printer()

# simple decorator

# def upper_decorator(function):
#     def wrapper():
#         func = function() # => "hello man!"
#         make_uppercase = func.upper() # => "HELLO MAN!"
#         return make_uppercase
#     return wrapper

# def say_hi():
#     return "hello man!"
# """
# upper_decorator() = wrapper  # withour calling it!
# so we have to call it one morem with using () brackets!
# like this: upper_decorator()()
# but its a bit confusing so you can call it with variable then call that variable 
# like this: new_name = upper_decorator() its equal to new_name  = wrapper
# so you can call it like new_name()
# """
# print(upper_decorator(say_hi)())

# """
# we have siple way to call it with "@"
# """
# @upper_decorator
# def sayHi():
#     return "hello bro!"

# print("its second method",sayHi())

# # split decorator 
# def split_func__(function):
#     def wrapper():
#         func = function()
#         splited = func.split(sep=" ")
#         return splited
#     return wrapper


# @split_func__
# @upper_decorator
# def sayHelleArray():
#     return "This hello man in array and its uppercase too its very cool!"

# print(sayHelleArray())

# def decorators_with_arguments(function):
#     def wrapper_accepting_arguments(arg1, arg2):
#         print("My argumetns are: {0}, {1}".format(arg1, arg2))
#         function(arg1, arg2)
#     return wrapper_accepting_arguments

# @decorators_with_arguments
# def cities(city_one, city_two):
#     print("Cities that i dream to live are {0} and {1}".format(city_one, city_two))

# cities("New York", "Californy")

# def decorator_test(function):
#     def wrapper(*args, **kwargs):
#         print("Positional arguments are:", args)
#         print("Keyword arguments are:", kwargs)
#         function(*args, **kwargs)
#     return wrapper

# @decorator_test
# def testing_decorator():
#     print("No arguments here!")

# @decorator_test
# def testing_decorator_(*a, **kwargs):
#     print("We have some arguments here!",kwargs["first_name"])

# testing_decorator()
# testing_decorator_(1,2,4,5,5, first_name = "Hanry")

from functools import wraps

def login_requires(local_data=""):
    def login_requires_decorator(func):
        @wraps(func)
        def wrapper(user_id):
            if user_id in local_data:
                return func(user_id)
            else:
                print("Please login in!")
        return wrapper
    return login_requires_decorator


@login_requires(local_data=[])
def change_password(user_id):
    print("your password has changed!")

new = change_password(12345)
