# Problem Solvind DAY 8

# Task
# Given  names and phone numbers, assemble a phone book that maps friends'
# names to their respective phone numbers. You will then be given an unknown number
# of names to query your phone book for. For each  queried, print the associated entry
# from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found,
# print Not found instead


# n = int(input())
# name_numbers = [input().split() for _ in range(n)]
# phone_book = {k: v for k,v in name_numbers}
# while True:
#     try:
#         name = input()
#         if name in phone_book:
#             print('%s=%s' % (name, phone_book[name]))
#         else:
#             print('Not found')
#     except:
#         break

#
# def rot_left(a, d):
#     nd = input().split()
#
#     n = int(nd[0])
#
#     d = int(nd[1])
#
#     a = list(map(int, input().rstrip().split()))
#     new_idx = d % len(a)
#     return a[new_idx:] + a[:new_idx]
#
#
# print(rot_left(a, d))

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * self.length + 2 * self.width
#
#
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)
#
#
# square = Square(4)
# print(square.area())


# Palindrome one line solution

# word ="wow"
#
# palindrome = bool(word.find(word[:: -1]) + 1)
#
# print(palindrome)

# Fibonaci series
#
# fibo = lambda n: n if n <= 1 else fibo(n - 1) + fibo(n - 2)
# result = fibo(10)
# print(result)


# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# print(fibo(5))
# 


# from abc import ABCMeta, abstractmethod
#
#
# class Book(object, metaclass=ABCMeta):
#     def __init__(self, title, author):
#         self.title=title
#         self.author=author
#     @abstractmethod
#     def display(): pass
#
# #Write MyBook class
# class MyBook(Book):
#     price = 0
#     def __init__(self, title, author, price):
#         super(Book, self).__init__()
#         self.price = price
#
#     def display(self):
#         print("Title: " + title)
#         print("Author: " + author)
#         print("Price: " + str(price))
#
#
# title = input()
# author = input()
# price = int(input())
# new_novel = MyBook(title, author, price)
# new_novel.display()

# class Difference:
#     def __init__(self, a):
#         self.__elements = a
#
#     def computeDifference(self):
#         self.maximumDifference = max(self.__elements) - min(self.__elements)
#
#     # Add your code here
#
#
# # End of Difference class
#
# _ = input()
# a = [int(e) for e in input().split(' ')]
#
# d = Difference(a)
# d.computeDifference()
#
# print(d.maximumDifference)

# ALGORITHMS

#  LINEAR SEARCH ALGORITHM
#
# def linear_search(lst, key):
#     position = 0
#     flag = False
#     while position < len(lst) and not flag:
#         if lst[position] == key:
#             flag = True
#         else:
#             position += 1
#     return flag
#
#
# lst = [65, 88, 123, 12, 3]
#
# found = linear_search(lst, 123)
# print("Element 123 is present: ", found)
#

# RECURSION

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# num = input("Enter number: ")
# n = int(num)
# f = factorial(n)
# print(f"Factorial {n}: ", f)

# Fibonacci

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# n = int(input(" Enter a number: "))
#
# print(f"Fibonacci {n}: ", fibonacci(n))

# Using Memoization and Decorators

# def memoize(f):
#     memo = {}
#
#     def helper(x):
#         if x not in memo:
#             memo[x] = f(x)
#         return memo[x]
#
#     return helper
#
#
# @memoize
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
#
#
# print(fib(100))

# BINARY SEARCH Iteratively
#
# def binary_search(lst, key):
#     low = 0
#     high = len(lst)-1
#     while low <= high:
#         mid = (high+low)//2
#         if key == lst[mid]:
#             return True
#         elif key < lst[mid]:
#             high = mid-1
#         else:
#             low = mid + 1

# def binary_search(lst, key): # the list has to be sorted
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         mid = (low+high)//2
#         if lst[mid] == key:
#             return True
#         elif key < lst[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1

#
# lst = [15, 21, 47, 84, 96]
# found = binary_search(lst, 15)
# print(found)

# def linear_search(lst, key): #the list can be unsorted
#     position = 0
#     flag = False
#     while position <= len(lst) and not flag:
#         if lst[position] == key:
#             return True
#         else:
#             position += 1
#     return flag



