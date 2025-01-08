km = int(input('Quantos Km foram percorridos? '))
dias = float(input('Por quantos dias o alugou? '))
total = (km * 0.15) + (dias * 60)
#preço = total (essa linha pode ser excluida, desnecessária, mas coloquei na 1ªx que fiz o cód.
print('O valor total a pagar será de R${:.2f}.'.format(total))
