""" Formatação de Strings"""

# Usar f para formatar. {função ou variável}. ou usar {} vazias e após aspas usar .format(função/variavél)
# {variável:.nf} sendo nf o número de casas decimais.
nome = "celso"
numero = 18.95252
print('Nome: {}, número editado para duas casas decimais {:.2f}.' .format(nome, numero))
'''Nome; celso, número editado para duas casas decimais 18.95.'''
