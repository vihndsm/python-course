#1 i=0
# while i<10:
#     i=i+1
#     print(i)

#2 i=0
# while i<20:
#     i=i+2
#     print(i)

#3 num=5
# a=int(input('enter your num:'))
# m=0
# while m<=10:
#     if a==num:
#         print('верно')
#         break
#     else:
#         a=int(input('enter your num:'))

#4 password=1234
# m=0 #count
# while m<3:
#     n=int(input('введите пароль'))
#     m=m+1
#     if n==password:
#         print("open")
#         break
#     if n!=password:
#         print("не верно повторите ввод")
#     if m==3:
#         print("вы потратили все попытки")

#5 a=int(input('number1:'))
# b=int(input('number2:'))
# c=int(input('number3:'))
# i = a
# d = 0
# while i < b:
#     i+=1
#     if i%c == 0:
#         d+=1
# print('Делимых на c чисел -',d)

#6 b=int(input('num:'))
# i=b
# while True:
#     print(i*'*')
#     i=i-1
#     if i<1:
#         break

#7 a=input('student:')
# b='exit'
# while True:
#     a=input('student:')
#     if a==b:
#         break

#8 a=int(input('age:'))
# i = 0
# while i < a:
#     if a % 2 == 0:
#         print(i+2)
#         i+=2
#     elif a % 2 == 1:
#         print(2+i-1)
#         # print(list(range(i)))
#         i+=2

#8 age = int(input('Age: '))
# a = 0 if age%2==0 else 1
# while a<=age:
#     print(a)
#     a+=2

#9 N=int(input('num:'))
# i=0
# while i<N:
#     i=i+1
#     if 2**i<N:
#         print(i, 2**i)
#     elif 2**i>=N:
#         break

"""# a=['C', 'H', 'Y', 'N', 'A', 'R']
# b=(str(input('enter your letter:')))
# c=a.index(b)
# count=0
# while True:
#     count += 1
#     b=(str(input('enter your letter:')))
#     c=a.index(b)
#     if count > 6:
#         print('Bye')
#         break
#     if c == 0:
#         print('C is 1st letter')
#         c=a.index(b)
#         continue
#     elif c == 1:
#         print('H is 2nd letter')
#         c=a.index(b)
#         continue
#     elif c == 2:
#         print('Y is 3rd letter')
#         c=a.index(b)
#         continue
#     elif c == 3:
#         print('N is 4th letter')
#         c=a.index(b)
#         continue
#     elif c == 4:
#         print('A is 5th letter')
#         c=a.index(b)
#         continue
#     elif c == 5:
#         print('R is 6th letter')
#         c=a.index(b)
#         continue
#     else :
#         print('not exist letter')"""
#10 s = 'github'
# c = 3
# ss = ''
# while c>0:
#     ss = input('введите: ')
#     if s.find(ss)>-1:
#        print(s.find(ss))
#     else:
#         c=c-1
#         print('неверно')

# print('попытки истрачены')