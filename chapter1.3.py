#1 a=[1, 1, 2, 3, 5, 8, [3, 2], 34, 55, 89]
# b=a.pop(6)
# c=a+b
# c.sort()
# print(c)
# for elem in c:
#     if elem < 5:
#         print(elem)

#2 a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b=[1, 2, 3, 4, 5,6, 7, 8, 9, 10, 11, 12, 13]
# result = []
# for elem in a:
#     if elem in b:
#         result.append(elem)
# print(result)

#3 a={2:1, 1:2, 3:1, 10:3}
# b={8:4, 4:1, 5:1, 9:5}
# c={11:6, 6:1, 12:7, 7:1}
# result = {}
# for d in (a, b, c):
#     result.update(d)
# print(result)

#4 numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
# for x in numbers:  
#     if x % 2 == 0:
#         print(x)
#     elif x == 237:
#             break

#5 a=int(input('first:'))
# b=int(input('second:'))
# print(list(range(a,b)))

#6 a=int(input('first num:'))
# b=int(input('second num:'))
# for i in range(a,b):
#     c=i**2
#     if c >=b:
#         break
#     print(c)

#7 a=[1,2,6,3,9,2,11,20,16,7,8]
# b=[] # b=0
# c=[] # b=0
# for i in a:
#     if i%2==1:
#         b.append(i)
#         # b+=1
#     elif i%2==0:
#         c.append(i)
#         # c+=1
# print('не четные: ', b)
# print('нечетные: ', c)

#8 for i in range(1,10):
#     print(str(i)*i)

#9 a=int(input('enter num:'))
# for i in range(1,11):
#     print(a, '*', i, '=', i*a)

#10 a=int(input('min:'))
# b=int(input('max:'))
# c=int(input('step:'))
# for n in range(a,b,c):
#     print(n)

#11 b=1 #fibonaci
# a=0
# n=int(input('enter num:'))
# summa=0
# for i in range(n):
#     summa = a+b
#     print(summa)
#     a=b
#     b=summa

#11 a=0
# b=1 #fibonaci
# n=int(input('enter num:'))
# i=2
# summa=0
# while i<=n:
#     summa = a+b
#     print(summa)
#     a=b
#     b=summa
#     i = i+1

# 11 a=1
# b=1
# for i in range(int(input('Ряд: '))):
#     print(a)
#     a = b
#     b = a+b

#12 a=1
# for i in range(1,int(input('Число: '))+1):
#     a*=i
# print(a)