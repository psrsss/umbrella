#Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
#Напишите программу, которая добавляет ‘ing’ к словам
# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
# Напишите программу которая удаляет пробел в начале, в конце строки
# Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"], "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
# Дан список: [Robin Singh], и 2 строки: "Welcome" и "airport". Напечатайте текст: “Hello, Robin Singh! Welcome to airport”
# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
S1 = 'www.my_site#about'
print(S1.replace("#", "/"))
S2 = 'This is a test message'
arr = S2.split()
S2 = "ing ".join(arr)
print(S2+"ing")
S3 = 'Ivanou Ivan'
done = " ".join(S3.split()[::-1])
print(done)
S4 = ' Hello '
print(S4[1:-1])
S5 = 'pARiS'
print(S5.capitalize())
S6 = 'Robin Singh'
S7 = 'I love arrays they are my favorite'
print(S6.split())
print(S7.split())
arr1 = ['Robin Singh']
Str1 = 'Welcome'
Str2 = 'airport'
print("Hello,", arr1[0] + "!", Str1, "to", Str2)
arr2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(arr2))
arr10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr10.insert(3, "new")
del arr10[6]
print(arr10)
