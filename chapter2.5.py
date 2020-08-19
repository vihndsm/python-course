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

