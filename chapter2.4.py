#1 def decorator(func):
#     def obertka(*args, **kwargs):
#         print('верхняя булочка')
#         func(*args, **kwargs)
#         print('нижняя булочка')
#     return obertka

# @decorator
# def chikken():
#     print('с курицей')
# chikken()
# @decorator
# def beef():
#     print('с говядиной')
# beef()
# @decorator
# def chile():
#     print('чили')
# chile()

# def bulochka(dec): #second version
#     def bul(*args, **kwargs):
#         print('Верхний булочка')
#         dec(*args, **kwargs)
#         print('Нижний булочка')
#     return bul

# def kotleta(k):
#     def kot(*args, **kwargs):
#         print('курчока')
#         k(*args, **kwargs)
#         print('говядина')
#     return kot

# @bulochka
# @kotleta
# def ingri(cheese, tomato, cucumbers, sous):
#   print(cheese,'\n', tomato,'\n', cucumbers,'\n', sous)

# ingri('Сыр','Помидор','Огурцы','Соус')

#2 def decorator(func):
#     def obertka(*args, **kwargs):
#         print('Результат выполнения вашей функции:',)
#         func(*args, **kwargs)
#     return obertka
# a=int(input('first num:'))
# b=int(input('second num:'))
# @decorator
# def multiple(a,b):
#     print(a+b)
# multiple(a,b)

# @decorator
# def min(a,b):
#     print(a-b)
# min(a,b)

#3 def decorator(func):
#     def obertka(*args, **kwargs):
#         print('крыша')
#         func(*args, **kwargs)
#         print('фундамент')
#     return obertka

# @decorator
# def home(*args):
#     for i in args:
#         print(i, end=' \n', )
# home('кухня','спальня','коридор','балкон')

# @decorator
# def flat(*args):
#     for i in args:
#         print(i, end=' \n', )
# flat('1-этаж','2-этаж','3-этаж','4-этаж')