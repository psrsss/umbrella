s1 = 'www.my_site#about'
print(s1.replace("#", "/"))
s2 = 'This is a test message'
arr = s2.split()
s2 = "ing ".join(arr)
print(s2+"ing")
s3 = 'Ivanou Ivan'
done = " ".join(s3.split()[::-1])
print(done)
s4 = ' Hello '
print(s4[1:-1])
s5 = 'pARiS'
print(s5.capitalize())
s6 = 'Robin Singh'
s7 = 'I love arrays they are my favorite'
print(s6.split())
print(s7.split())
arr1 = ['Robin Singh']
str1 = 'Welcome'
str2 = 'airport'
print("Hello,", arr1[0] + "!", str1, "to", str2)
arr2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(arr2))
arr10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr10.insert(3, "new")
del arr10[6]
print(arr10)
