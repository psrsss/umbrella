"""Этот модуль выполняет домашнее задание №6"""
S1 = 'www.my_site#about'
print(S1.replace("#", "/"))
S2 = 'This is a test message'
arr = S2.split()
S2 = "ing ".join(arr)
print(S2+"ing")
S3 = 'Ivanou Ivan'
DONE = " ".join(S3.split()[::-1])
print(DONE)
S4 = ' Hello '
print(S4[1:-1])
S5 = 'pARiS'
print(S5.capitalize())
S6 = 'Robin Singh'
S7 = 'I love arrays they are my favorite'
print(S6.split())
print(S7.split())
arr1 = ['Robin Singh']
STR1 = 'Welcome'
STR2 = 'airport'
print("Hello,", arr1[0] + "!", STR1, "to", STR2)
arr2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(arr2))
arr10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr10.insert(3, "new")
del arr10[6]
print(arr10)
