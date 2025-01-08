tab = int(input('Qual a tabuada:\n'))
print(f'A tabuada de {tab} é:')
for i in range(1, 11):
    print(f'{tab} x {i} = {tab * i}')
