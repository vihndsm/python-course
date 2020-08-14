#1 p = open('text.txt', 'r') # открыть в режиме чтение
# a = p.read()
# print(a)
# p.close()

#2 with open('text1.txt', 'r') as a: #построчно читать файл и сохранять его в виде списка
#     b = a.readlines()
#     print(b)

#3 p = open('text.txt', 'r') # открыть в режиме чтение cтрока за строкой читала файл
# for line in p:
#         print(line)

#4 with open('text.txt') as f: #найти самые длинные слова.
#   a = f.read().split()
#   print(max(a, key=len))

#5 with open('text1.txt') as a: #подсчета количества строк в текстовом файле
#     print(len(a.readlines()))

#6 s = ['Aito','Kirill','Taalai','Umut'] #перевести список по строкам
# s = [i + '\n' for i in s]
# with open('text1.txt','w') as f:
#     f.writelines(s)
#     # print(f.read())

#7 p = open('text.txt', 'w') # открыть в режиме чтение
# p.close()
# print('Возвращает True если файл был закрыт: ', p.closed)

#8 with open('text.txt') as f: #подсчета количества слов в текстовом файле
#     print(len(sorted(f.read().split())))
