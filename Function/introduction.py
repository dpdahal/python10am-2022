# function two types
# inbuilt function
# user defined function

# inbuilt function
# abs()
# print()
# input()
# dir()
# help()

# define function
# def users():
#     # function body part
#     print("I am users function")
#
#
# # call function
# users()


# def add(x, y):
#     return x + y
#
#
# print(add(20, 30))
# print(add(56, 30))
# add
# sub
# mul
# div
# modules
# WAP to check enter number ever or odd
# def test(a):
#     print(a)
# c = int(input("enter the number"))
# test(c)

#
# def users(name, age):
#     print("Name:", name)
#     print("Age:", age)
#
#
# users("John", 20)
# users("Sophia", 50)
# * args
# ** kwargs

# def students(*names, **data):
#     print(names)
#     print(data)
#
#
# students('ram', 'shyam', 'hari', name='ram', age=20)

# def test():
#     return "hello"
#
#
# print(test())

# def get():
#     return "I am get"
#
#
# def post():
#     print(get())
#
#
# post()
#
# def take_value():
#     p = int(input("enter p: "))
#     t = int(input("enter t: "))
#     r = int(input("enter r: "))
#     return [p, t, r]
#
#
# def calculate():
#     data = take_value()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p * t * r / 100
#
#
# def display():
#     return calculate()
#
#
# print(display())


# def my_rep(data,times):
#     return data * times
#
# print(my_rep('ram',3))

# def my_rep(data, times):
#     increment = 0
#     while increment < times:
#         print(data)
#         increment += 1
#
#
# my_rep('ram', 3)
#
# print("1.Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.Mac(Rs:40000)")
#
#
# def dell():
#        # qunatity
#     q = int(input("enter the quantity: "))
#
# def toshiba():
#     pass
#
#
# def mac():
#     pass


#
# def kalanki():
#     pass
#
# def chabile():
#     pass


# def test():
#     return "test"
#
# print(test)

# 5 = 120

# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
#
# print(fac(5))

# 5-1 =4*5 =20
# 4-1 =3*20 =60
# 3-1 =2*60 =120
#

x = 10


def test():
    global x
    x = x + 30
    print(x)


test()

print(x)
