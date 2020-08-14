# str = input('введите сиболы: ')
# if str == str[::-1]:
#    print('True')
# else:
#    print("False")

# с = input()
# l = len(с)
# l = l//2
# for i in range(l):
#     if с[i] != с[-1-i]:
#         print("False")
#         quit()
# print("True")
# input()

# 2 a=['a', 'b', 'c', 'a', 'b', 'c']
# b=a.index('a')
# c=a.index('c')
# print(b, c)

# 3 a=int(input())
# b=int(input())
# c=int(input())
# print('sum:', a+b+c)

# 4 d=[]
# d.append(str(input('enter: ')))
# a=0
# while a<4:
#     d.append(str(input('enter: ')))
#     a+=1
# c=sorted(d)
# print(' '.join(c))

# 5 s = 'Hello World'
# ss = str(input('enter:'))
# if s.find(ss)>-1:
#     print('Hello')
# else:
#     print('bye')

#5 print('Hello' if 'Hello World'.find(input('Letter: '))>-1 else 'Bye')

#6 a = [i for i in range(1500,2700) if i%5 == 0 
# or i%7 == 0]
# print(a)

#6 a=1499
# while a<=2700:
#     a+=1
#     if a%7==0:
#         print(a)
#     elif a%5==0:
#         print(a)

# 7 b=[]
# a=0
# while a<=6:
#     b.append(a)
#     a+=1
# print(b)
# for i in b:
#     if i == 3:
#         b.remove(3)
#         continue
#     elif i==6:
#         b.remove(6)
# print(b)


# 8 i=0
# while i<6:
#     a=str(input('enter the letter:'))
#     print(a.upper())
#     i+=1
    
#9 a=input('text:')
# num = [int(i) for i in a if i.isdigit()]
# letter = [str(i) for i in a if i.isalpha()]
# print('Количество цифр в тексте:', len(num))
# print('Количество буквы в тексте:', len(letter))

#10 word = input(str())
# гласные = 0
# согласные = 0
# for i in word:
#     letter = i.lower()
#     if letter == "a" or letter == "e" or\
#        letter == "i" or letter == "o" or\
#        letter == "u" or letter == "y":
#         гласные += 1
#     else:
#         согласные += 1
# print("глачные %i\nсогласные %i" % (гласные, согласные))

# b=[]
# a=input('вводите только целые числа или слово "end":')
# c='end'
# while True:
#     b.append(int(a))
#     a=input('вводите только целые числа или слово "end":')
#     if a==c:
#         break
# average=sum(b) / len(b)
# print('You entered: ', b)
# print('Total: ', sum(b))
# print('Average: ', average)

#12 d=[]
# a=input('Enter your name: ')
# d.append(a)
# b=input('Enter you last name: ')
# d.append(b)
# c=int(input('When were you born? '))
# f=2018-c
# d.append(f)
# e=input('Where are you from? ')
# d.append(e)
# print('Hello',a,b'.  You are',f,'years old.', 'You are living in',e)

#12 print('Hello,',input('Name:'),input('Surname:'),'.You are',2018-int(input('Born:')),'years old.','You are living in',input('Country:'))

#13 yoda=['on Python', 'programming', 'I like']
# print(yoda[::-1])

#14 marks = {}
# stud = ['John','Jane','Bill','Mary']
# mark = [5,2,5,5]
# for i in range(4):
#     marks.update({stud[i]:mark[i]})
# print(int(sum(list(marks.values()))/4)+1)

#14 d=[]
# a=int(input('Enter mark for Bill: '))
# d.append(a)
# b=int(input('Enter mark for Jane: '))
# d.append(b)
# c=int(input('Enter mark for John: '))
# d.append(c)
# e=int(input('Enter mark for Mary: '))
# d.append(e)
# average=int((sum(d) / len(d))+0.5)
# print('Average mark:', average)