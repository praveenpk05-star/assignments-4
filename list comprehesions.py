#List with only even numbers up to 20
print('even nos:',[i for i in range(21) if i%2 == 0])
#List with only odd numbers up to 20
print('odd nos:',[i for i in range(21) if i%2 != 0])
#List with squares up to 20
l = list()
for i in range(1, 21):
    l.append(i ** 2)
print('squares:',l)
#List with Cubes up to 20
l = list()
for i in range(1, 21):
    l.append(i ** 3)
print('Cubes:',l)

