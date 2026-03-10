#Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
#Напишите программу, которая добавляет ‘ing’ к словам
# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
# Напишите программу которая удаляет пробел в начале, в конце строки
# Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"], "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
# Дан список: [Robin Singh], и 2 строки: "Welcome" и "airport". Напечатайте текст: “Hello, Robin Singh! Welcome to airport”
# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
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
