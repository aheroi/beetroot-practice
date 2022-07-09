print("""  Hello,
            I'm here

""")

s = 'hello\
Hello'
print(s)

s = 'Hello, \'New York\''
print(s)

s = 'Hello, \'New York\''

a = 'helllo'
print(a.count('l'))
print(a.upper(), end='!!!') 

a = a + '!!!'
print(f'\nnew a: {a}')


s = 'Hello Hello Hello'
print(s.replace('ll', 'LLL'))

print('12344j'.isdigit())
print('12344j'.isalpha())
print('1234566799'.isdigit())
print('qWErTTYu'.isalpha())

s = 'Hellllo Helllleee'
print(s.replace('lll', 'AAAAA'))

print('he' in 'HELLo')
print('he' in 'heLLo')

s_str = 'Hello'
print(s_str.index('e'))
print(s_str.index('o'))
print(s_str.find('h'))
print(s_str.find('ll'))
print(s_str.rfind('l'))
print(s_str.find('l'))

print(s_str[1])
print(s_str[1:3])
print(s_str[1:5:3])
print(s_str[:])
print(s_str[-1:len(s_str)])
print(s_str[3:-1])

print(s_str.strip())
print(s_str.isspace())
print(s_str.startswith('H'))
print(s_str.endswith('o'))
print(s_str.find('H'))
print(s_str.replace('Hel', 'hELLO'))
print(s_str.split())
print('--'.join(['H', 'e', 'll', 'O']))
print(s_str[:3])
print(s_str[3:])
print(s_str[:3] + s_str[3:])



