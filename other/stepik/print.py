print(1234)
print(1, 2, 3, 4)
print('hello', True, 21)
print(2+3, 4*5, 2+3*4)

a = 100
b = 200
print(a, '+', b, '=', a + b)
print(a, ' * ', b, ' = ', a * b)

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep=' ')
print(1, 2, 3, 4, sep='')
print(1, 2, 3, 4, sep=',')
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='###')

print(1, 2, 3)
print('hello', end='\n')
print(4, 5, 6)
print('new hello')
print(7, 8, 9)

print(1, 2, 3, end='!') #не будет переноса в конце
print('hello') # здесь будет перенос
print(5, 6, 7) # и здесь будет перенос

print(1, 2, 3, sep='!', end='?')
print('new', 'string')
print(5, 6, 7, 8, 9, end='END', sep='@') # и здесь будет перенос


