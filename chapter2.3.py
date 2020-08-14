#1 try:
#     a = input('enter first num:')
#     b = input('enter second num:')
#     result = int(a) / int(b)
# except ValueError:
#     print('only integer')
# else:
#     print('result is:', result)

#2 user = input('Введите имя: ')
# my_list = ['Taalay', 'Kirill', 'Turat', 'Umut', 'Aito', 'Adinai', 'Aleksandr']
# while True:
#     try:
##         my_list.remove(user)
#         print('Welcome')
#         user = input('Введите имя: ')
#     except:
#         print('Bye')
#         break

#3 try:
#     z = {1:'key1', 2:'key2', 3:'key3'}
#     a=int(input('enter your code:'))
#     z.pop(a) # удаление элемента словаря
# except KeyError:
#     print('не правильно ввели ключ!')
# else:
#     print(z)

#4 try:
#     a = input('enter first num:')
#     b = input('enter second num:')
#     result = int(a) / int(b)
# except ValueError:
#     print('only integer')
# except ZeroDivisionError:
#     print('non divided by zero')
# else:
#     print('result: ', result)
# finally:
#     print('excellent!')

# try:
#     a = ['T', 'U', 'R', 'A', 'T', 'B', 'E', 'K']
#     b = input('введите букву:')
#     c = a.index(b) #определение первого элемента с лева
# except IndexError:
#     print('такая буква нету в списке!')
# except ValueError:
#     print('введите только латынские БОЛЬШИЕ буквы')
# else:
#     print('буква по индексу:',c)
# finally:
#     print('Проверка завершена')