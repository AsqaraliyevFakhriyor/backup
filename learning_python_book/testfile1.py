
""" Working with files in python """
# f = open("filename", "w")
# f.read()
# f.write()

""" Types """
# decimal, and fraction


""" Python classes """


# class Worker:
#     def __init__(self, name, pay):
#         self.name = name
#         self.pay = pay

#     def lastName(self):
#         return self.name.split()[-1]

#     def giveRaise(self, percent):
#         self.pay *= (1.0 + percent)

    
# bob = Worker("Bob Smith", 50000)
# sue = Worker("Sue Jones", 60000)


""" Numberic types of python2 """

# pow(2, 2) -> 8 == sqr
# hex() -> 16 lik sanoq sistemasi
# oct() -> 8 lik sanoq sistemasig otkazish
# bin() -> binary code shakliga otgazis {faqat number}

# Type testing 
# as_integer_ratio
# is_integer
# bit_length

# from __future__ import division -> LoL


# import math
# math.floor(2,5) -> 2 
# math.floor(-2,5) -> -3
# 
# math.trunc(2.5) -> 2
# math.trunc(-2,5) -> -2 


# class Candidate:

#     def __init__(self, name, age, gender, direction):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.direction = direction

#     def getInfo(self):
#         return "Candidate: {0}\nage: {1}\ngender: {2}\ndirection: {3}".format(self.name, self.age, self.gender, self.direction)

#     def whenBorn(self, cur_year):
#         born_in = cur_year - self.age
#         return born_in


# import sys
# print(sys.argv)
# if "-f" in sys.argv:
#     print("force activated")

# s = 'sPAM!sPAM!sPAM!sPAM!sPAM!sPAM!sPAM!sPAM!sPAM!sPAM!'
#  s.swapcase() => "Span!" -> "sPAN!"
# 
# 
# 

# def uppercase(s):
#     return s.upper()

# print(list(map(uppercase, s)))