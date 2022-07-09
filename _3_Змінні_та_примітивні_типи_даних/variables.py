from operator import le


message = 'Hello, World!'
print(message)

lang_1 = 'python'
lang_2 = 'java'
lang_3 = 'C++'
print('Program language:' +'\n\t'+ lang_1.title() + '\n\t' + lang_2.title() + '\n\t' + lang_3.title())

name = 'Carl Johnson'
print(name)
initials = name[0] + name[5]
print('Task:')
print(name[0:5].title() + initials + ' '+ name[5:len(name)].title())

a, b = 2, 3
print(a ** b)
a *= 3
print(a)