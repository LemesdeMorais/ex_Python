produto = float(input('Qual o valor do produto? R$'))
desconto = (produto*5) / 100
total = produto-desconto
print('O produto custa R$ {:.2f}, o desconto de 5% fica em R$ {} e no total de R$ {:.2f}.'.format(produto,desconto, total))
"""
outro jeito de fazer o mesmo algoritimo

preço = float(input('Qual o valor do produto? R$))
novo = preço - (preço*5/100)
print('O produto que custava R${}, na promoção de 5% vai custar R${}'.format(preço,novo))
"""

