# class Emplyee:
#     name = 'name'
#     lastname = 'lastname'
#     position = 'pos'
#     salary = 'sal'
#     def get_info(self, name, lastname, position, salary):
#         self.name = input('name: ')
#         self.lastname = input('surname: ')
#         self.position = input('pos: ')
#         self.salary = int(input('salary: '))

# a = Emplyee()
# a.get_info(1,2,3,4)
# print(a.name, a.lastname, 'работает на должности:', a.position, 'получает зарплату в размере:', a.salary)

# class Emplyee:
#     name = 'name'
#     lastname = 'lastname'
#     position = 'pos'
#     salary = 'sal'
    
#     def get_info(self, name, lastname, position, salary):
#         self.name = name
#         self.lastname = lastname
#         self.position = position
#         self.salary = salary

# a = Emplyee()
# a.get_info(name=input('name:'), lastname=input('lastname:'), position=input('position:'), salary=int(input('salary:')))
# print(a.name, a.lastname, 'работает на должности:', a.position, 'получает зарплату в размере:', a.salary)

############################################################################################################
# class Person:
#     name = 'default'
#     apple = '1'

#     def set(self, name, apple):
#         self.name = name
#         self.apple = apple

# a = Person()
# a.set('Aito', 1)
# b = Person()
# b.set('Kilill', 2)
# c = Person()
# c.set('Taalai', 3)
# d = Person()
# d.set('Turat', 4)
# e = Person()
# e.set('Umut', 5)
# print(a.name, a.apple, b.name, b.apple, c.name, c.apple, d.name, d.apple, c.name, c.apple, e.name, e.apple,)
# print('общая сумма яблок всех детей: ', a.apple+b.apple+c.apple+d.apple+e.apple)

###########################################################################################################

# class Shop:
#     name = 'name'
#     is_open = 'yes'
#     product_list = 'list'

#     def add_products(self, name, is_open, product_list):
#         self.name = input('name:')
#         self.is_open = True
#         self.product_list = int(input('product:'))

# a = Shop()
# a.add_products(1,2,3)
# if a.product_list > 0:
#     a.is_open = True
# else:
#     a.is_open = False
# print(a.name, a.is_open, a.product_list)

############################################################################################################