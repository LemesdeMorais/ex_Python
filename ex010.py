real = float(input('Quanto dinheiro você tem na cardeira? R$'))
dolar = real / 6.103
euro = real / 6.31
iene = real / 0.042
print('Com R$ {:.2f} você pode comprar \n US${:.2f}\n {:.2f} Euros \n {:.2f} Iene(s)'.format(real, dolar,euro,iene))

