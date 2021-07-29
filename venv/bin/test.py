# # def compute_grade(score):
# #     if score >= 0.9:
# #         return "A"
# #     elif score >= 0.8:
# #         return "B"
# #     elif score >= 0.7:
# #         return "C"
# #     elif score >= 0.6:
# #         return "D"
# #     elif score < 0.6:
# #         return "F"
# #     else:
# #         return "Bad Score"
# #
# #
# # score = float(input("Enter score: "))
# # print(compute_grade(score))
#
#
# # A = [1,4,9,16,25,36,49,68,81,100]
#
# fruits = [2, 3, 4, 5, 6, 7, 8, 9]
# newlist = [x for x in fruits if x % 2 == 0]
#
# print(newlist)
# newLi = [x * 2 for x in fruits if x >= 5]
#
# print(newLi)
#
#
# # list comprehension - [value stored, the iteration, the condition]
#
#
# def is_palindrome(word):
#     return word == word[::-1]
#
#
# print(is_palindrome("tree"))
#
# name = input("Enter your name: ")
# print(name[::-1])
#
# thistuple = ("apple", "banana", "cherry")
# thilist = ["apple", "banana", "cherry"]
# print(thistuple)
# turpl = (1,)
# print(type(turpl))
#
# dict = {1: "kim", 2: "colo"}
#
# thisset = {"apple", "banana", "cherry", "apple"}
#
# thisset.add("kiwi")
# thisset.remove("cherry")
# print(thisset)
#
# coordinates = {(0, 0): 100, (1, 1): 200}
# coordinates[(1, 0)] = 150
# coordinates[(0, 1)] = 125
#
# print(coordinates)
#
# names = ["f", "dry", "xdd", "drt", "drd"]
# for name in names:
#     print(name)
#
# speed = {"jan": 47, "feb": 52, "march": 47, "april": 44, "may": 52, "june": 53, "july": 54, "aug": 44, "sept": 54}
# speed1 = list(set(speed.values()))
# print(speed1)

for x in range(0, 100):
    if x % 7 == 0 and not x % 5 == 0:
        print(x, end=",")

# usernam@companyname.com
email = "washi@ifix.com"
em = email[email.index("@")+1 : email.index(".")]
uname = email[]
print(email[uname])
#start, end, step
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(3)
# print(a[x])

# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(2, 7, 2)
# print(a[x])
# contai= (0, 1, 2)
# result1 = slice(3)
# print(result1)