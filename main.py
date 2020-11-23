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

fibo = lambda n: n if n <= 1 else fibo(n - 1) + fibo(n - 2)
result = fibo(10)
print(result)




