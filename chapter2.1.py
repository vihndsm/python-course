#1 def num(x, y, z): # самое большое значение
#     if x>y>z:
#         print(x)
#     elif z>x:
#         print(z)
#     else:
#         print(y)
# x=int(input('num1:'))
# y=int(input('num2:'))
# z=int(input('num3:'))
# num(x, y, z)

#2 def num(x):
#     print(x)
# x=(1,2,3,4,5)
# num(sum(x))

#3 def factorial(x):
#     print(x)
# x=int(input('num:'))
# for i in range(1, x):
#     x*=i
# factorial(x)

#4 def abc(x):
#         if a>1:
#             print('yes')
#         else:
#             print('No')
# x='dsad45678jlkj'
# num = input("Введите число: ")
# a= x.find(str(num))
# abc(x)

#5 def cd(x):
#     b=[]
#     c=[]
#     for i in x:
#         if i.isupper() == True:
#             i = b.append(1)
#         else:
#             i = c.append(1)
#     print('количество символов в верхнем регистре:', len(b))
#     print('количество символов в нижнем регистре:', len(c))
# x = 'Быстрый Brow Fox'
# cd(x)

#6 def abc(x):
#     if x.isnumeric():
#         num = int(x)
#         print(num)
#     else:
#         print('не простое число!')
# x = input("Введите число: ")
# abc(x)

#7 def math(a,b,c):
#     if c =='+':
#         print(a+b)
#     elif c=='-':
#         print(a-b)
#     elif c=='*':
#         print(a*b)
#     elif c=='/':
#         print(a/b)
#     else:
#         print('Error')
# a=int(input('num1: '))
# b=int(input('num2: '))
# c=input('operation: ')
# math(a,b,c)

#8 def leap(a):
#     if a in b:
#         print('True')
#     else:
#         print('False')
# a=int(input('enter the year: '))
# b=list(range(4,5100,4))
# leap(a)

#10 def season(e):
#     if e in a:
#         print('зима')
#     elif e in b:
#         print('весна')
#     elif e in c:
#         print('лето')
#     elif e in d:
#         print('осень')
# a=['декабрь', 'январь', 'февраль']
# b=['март', 'апрель', 'май']
# c=['июнь', 'июль', 'август']
# d=['сентябрь', 'октябрь', 'ноябрь']
# e=str(input('месяц: '))
# season(e)

#11 def last(a):
#     print('last letter:', a.split(b))
# a=str(input('type: '))
# b=a[:-1]
# last(a)

#12 def num(x, y, z): # самое большое значение
#     if x>y>z:
#         print(x)
#     elif z>x:
#         print(z)
#     else:
#         print(y)
# x=int(input('num1:'))
# y=int(input('num2:'))
# z=int(input('num3:'))
# num(x, y, z)

#13 def polin(a):
#     if a == a[::-1]:
#         print('палиндром')
#     else:
#         print('не палиндром')
# a=input('type: ')
# polin(a)

# def time(x):
#     a=[]
#     if x <= 60:
#        a.append(60/x)
#     elif x <= 3600:
#         a.append(3600/x)
#     elif x <= 86400:
#         a.append(86400/x)
#     print(a)
# x=int(input('Enter the number of seconds:'))
  
# time(x)

#14 from datetime import datetime, timedelta

# def GetTime():
#     sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
#     d = datetime(1,1,1) + sec

#     print("DAYS:HOURS:MIN:SEC")
#     print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))
# GetTime()

# def sport(a):
#     if b in a:
#         print(a.get(b), 'место')
#     else:
#         print('такого участника нету!')
# b=str(input('имя:'))
# a={'Bolt':1, 'Me':2, 'Aibek':3}
# sport(a)

# def sprt(d):
#     if c in d:
#         print(d.get(c), c,'- место')
#     else:
#         print('тольки три участника!')
# c=int(input('место:'))
# d={1:'Bolt', 2:'Me', 3:'Aibek'}
# sprt(d)