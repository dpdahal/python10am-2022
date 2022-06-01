# user defined function

# normal function

# def test():
#     print("hello world")
#
#
# test()

# function accept value


# def user(name, age):
#     print("hello", name, age)
#
#
# user('ram', 200)


# optional value in function

# def users(name, age=0):
#     print("hello", name)
#     print("age", age)
#
#
# users('ram', 20)

# def uses(*name, **data):
#     print(name)
#     print(data)
#
# uses()


# function return value

# def test():
#     a = 10
#     if a % 2 == 0:
#         return "even"
#     else:
#         return "odd"
#
#
# print(test())


# def data():
#     a = 10
#     b = 20
#     return [a, b]


# local
# global
# x = 30
#
#
# def test():
#     x = 10
#
#
# test()

# def test():
#     print('inside test')
#
# print(test)


# a = lambda x, y: x + y
#
# print(a(10, 30))

# def out():
#     def inside():
#         return "inside"
#
#     return inside
#
# a = out()
# print(a())
# print(out()())
# print(out())


# def users():
#     def name(new_name):
#         return new_name
#
#     return name
#
#
# a = users()
# print(a('ram'))


# def test():
#     """
#     this is a test function
#   """
#     return "Welcome test function"
#
# # print(test())
# print(test.__doc__)
# print(test.__name__)

# def get_doc(any_function_here):
#     def inner_function():
#         return any_function_here.__doc__
#
#     return inner_function
#
#
# @get_doc
# def users():
#     """i am users function"""
#     return "Welcome"
#

# print(users())


def zero_check(any_function):
    def inner_function(x, y):
        if y == 0:
            return "Y is zero"

        else:
            return any_function(x, y)

    return inner_function


@zero_check
def add(x, y):
    return x + y


print(add(10, 0))

# module

