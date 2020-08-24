#1 class Animal:
#     name = 'default'
#     hunger = 5
#     def eat(self, name, hunger):
#         self.name = input('name: ')
#         self.hunger = hunger

# class Cat(Animal):
#     m = 1
#     def meow(self, m):
#         self.m = int(input('meow: '))
# a = Cat()
# a.eat(1, 2)
# a.meow(1)
# class Dog(Animal):
#     n = 1
#     def bark(self, n):
#         self.n = int(input('bark: '))
# b = Dog()
# b.eat(1, 2)
# b.bark(1)

# while a.name == 'cat':
#     if a.m > 5:
#         print('Кошка хочет поесть! Мяукает', a.m, 'раз')
#         for x in range(5, a.m):
#             user = input('Накормите кошку: ')
#             print('Кошка мяукает')
#         break
#     else:
#         print('Кошка спокойна и довольна, сыта))')
#         break
# else:
#     print('Вы не правильно ввели название животного!')
# while b.name == 'dog':
#     if b.n > 5:
#         print('Собака хочет поесть! Лает', b.n, 'раз')
#         for x in range(5, b.n):
#             user = input('Накормите собаку: ')
#             print('Собака лает')
#         break
#     else:
#         print('Собака спокойна и довольна, сыта))')
#         break
# else:
#     print('Вы не правильно ввели название животного!')


#2 class Car:
#     make = 'Germany'
#     model = 'cla'
#     year = 2017
#     petrol = 70
#     def drive(self, make, model, year, petrol):
#         self.make = input('country:')
#         self.model = input('model:')
#         self.year = int(input('date:'))
#         self.petrol = int(input('petrol:'))
# car = Car()
# car.drive(1,2,3,4)
# print('страна:', car.make, '\nмарка:', car.model, '\nгод выпуска:', car.year, '\nбензин в баке:', car.petrol)
# class Add(Car):
#     odometer = 0
#     def __dictance(self, odometer):
#         self.odometer = car.petrol*10
# abc = Add()
# abc._Add__dictance(1)
# print('на', abc.odometer,' км хватает бензина')
# class Subtract(Car):
#     petrol = 0
#     def __fuel(self, petrol):
#         self.petrol = petrol
# AU = Subtract()
# AU._Subtract__fuel(int(Car.petrol - int(input('dictance:'))*10))
# print('осталось', AU.petrol, 'литр бензина')
# if  AU.petrol > 0:
#     print('Let’s drive!')
# else:
#     print('недостачно бензина!')

#3class List:
#     name = 'default'
#     contact = 'IT'
#     address = '18'
#     def set(self, name, address, contact):
#         self.name = name
#         self.contact = contact
#         self.address = address
# Taalai = List()
# Taalai.set('Taalai', 222, 'мкр Джал')
# Umut = List()
# Umut.set('Umka', 111, '10 мкр')
# Aito = List()
# Aito.set('Aito', 333, '3 мкр')
# Kirill = List()
# Kirill.set('Kirill', 444, '4 мкр')
# Turat = List()
# Turat.set('Turatbek', 555, '5 мкр')
# class Contactlist(List):
#     name= 'Aito'
#     def search_by_name(self, name):
#         self.name = 1
# all_contact = [Taalai, Umut, Aito, Kirill, Turat]
# all_contact = Contactlist()
# all_contact.search_by_name(1)
# for i in range(0,6):
#     all_contact.name = str(input('name: '))
#     if all_contact.name == 'Aito':
#         print(Aito.name, Aito.contact, Aito.address)
#     if all_contact.name == 'Taalai':
#         print(Taalai.name, Taalai.contact, Taalai.address)
#     if all_contact.name == 'Umut':
#         print(Umut.name, Umut.contact, Umut.address)
#     if all_contact.name == 'Kirill':
#         print(Kirill.name, Kirill.contact, Kirill.address)
#     if all_contact.name == 'Turat':
#         print(Turat.name, Turat.contact, Turat.address)


#4 class House:
#     t = 'default'
#     s = '18'
#     def area(self, t, s):
#         self.t = input('тип дома: ')
#         self.s = int(input('площадь дома: '))

# class Furniture(House):
#     locker = '2'
#     table = '1.5'
#     bed = '4'
#     def abc(self, locker, table, bed):
#         self.locker = 2
#         self.table = 1.5
#         self.bed = 4
# a = Furniture()
# a.area(1, 2)
# a.abc(1, 2, 3)
# g = ['кровать', 'шкаф', 'стол']
# print('тип дома: ', a.t, 'площадь дома: ', a.s, '\nсписок мебели внутри дома: ', g)
# f=(a.s - (a.locker+a.table+a.bed))
# if f > 0:
#     print('осталось', f, 'кв.м свободных мест')
# else:
#     print('нет места для мебели')
