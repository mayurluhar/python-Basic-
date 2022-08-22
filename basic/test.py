# prices = [49, 249, 349, 449, 799]
# print(prices[-4], prices[-5:-2], prices[-3:-4])

# int_a = 3
# float_a = 3.0
# if int_a < float_a:
#     print("False")
# elif int_a > float_a:
#     print("True")

# class Math:
#     def __init__(self, num):
#         self.num = num
# class Number(Math):
#     def __init__(self, num):
#         self.value = num * 2
#     def show(self):
#         print(self.value, self.num)
#
# obj = Number(10)
# obj.show()

# nums1 = (6, 2, 0, 0)
# nums2 = (5, 2, 3, 4)
#
# print(nums1 > nums2)

#
# try:
#     print(14/0)
#     print("88"+1)
# except (NameError, TypeError):
#     print("Invalid input")

# import requests as rq
# import bs4
#
# res = rq.get('https://en.wikipedia.org/wiki/Herman_the_Archdeacon')
#
# soup = bs4.BeautifulSoup(res.text, 'lxml')
#
# for i in soup.select('.toc'):
#     print(i.text)

# heros = list()
#
# #
# while (takeHeros := input("Enter Name")) != "q":
#     heros.append(takeHeros)
#
# print(heros)
#
# myTags = ("Name", "Last_Name", "Age", "Phone")
#
# myOne = dict.fromkeys(myTags)
#
# print("My Dictionary is: %s" %str(myOne))


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 == 0):
        if n > 3:
            print("Not Weird")
        elif n > 3:
            print("Weird")
        else:
            print("Not Weird")

    else:
        pass

