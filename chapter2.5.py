#1 a = lambda g, h: g+h
# b = int(input('enter the num:'))
# print(a(b, 15))
# z = lambda x, y: x*y
# print(z(34, 32))

#2 a = lambda g, h: g*h
# b = int(input('enter the num:'))
# print(a(b, 15))

#3 g = [1, 2, 3, 2.1, 2.3, -1, 0]
# f = list(filter(lambda a: a > 0, g)) # функция для фильтрации списка целых чисел
# print(f)

#4 a = lambda g, h: g**h #которая возводит в квадрат каждое число
# b = int(input('enter the num:'))
# print(a(b, 2))
# a = lambda g, h: g**h
# b = int(input('enter the num:')) #которая возводит в куб каждое число
# print(a(b, 3))

#5 a=[1, 2, 3, 2.1, 2.3, -1, 0]
# b=[2, 5, 7, 2, 6]
# z = lambda g, h: g+h
# print(list(set(z(a, b))))

#6 g = [1, 2, 3, 5, -2, -1, -4]
# f = list(filter(lambda a: a > 0, g)) # перестановки положительных и отрицательных 
# h = list(filter(lambda b: b < 0, g))
# print(f,'\n',h)

#7 a = [1,2,3,4,5,6,7,8,9,10]
# f = list(filter(lambda b: b/2 in a, a))
# g = list(filter(lambda b: b%2 in a, a))
# print(f, g)

#8 g = ['poisk', 'google', 'microsoft', 'spaceX']
# f = ['neirolink', 'FACEBOOK', 'WHATSAPP']
# c = list(map(lambda g,f: g +' ' + f,g,f))
# print(c)

#9 a = [1,2,9,3,8,4,5,11,0,15]
# result = map (lambda x: x*x, a)
# print(list(result))

#10 g = [1, 2, 3, 5, -2, -1, -4]
# h = list(filter(lambda b: b < 0, g))
# b = sum(h)
# print(h,'\nсумма отрицательных чисел:',b, '\nабсолютное значение',abs(b))

#11 c = [39.2, 36.5, 37.3, 37.8]
# F = list(map(lambda x: x * (9/5) + 32, c))
# print(F)
# Celsius = [39.2, 36.5, 37.3, 37.8]
# Fahrenheit = list(map(lambda x: (float(9)/5)*x + 32, Celsius))
# print(Fahrenheit)
# C = list(map(lambda x: (float(5)/9)*(x-32), Fahrenheit))
# print(C)

#12 f = [1,2,3,4,5,6,7,8,9]
# a = list(map(lambda x : True if not x % 2 else False,f))
# b = list(map(lambda x : x % 2 == False,f))
# print(a,'\n', b)