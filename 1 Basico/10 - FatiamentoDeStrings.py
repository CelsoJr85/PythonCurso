"""Fatiamento de Strings"""

# Len informa todas as letras e caracteres da string
nome = "Celso Custodio"
print(len(nome))
'''14 (Pois tem 14 caracteres no nome Celso Custodio, incluindo o espaço no meio.)'''

# Fatiamento [i:f:p] [::] (i = início = 0, f = fim, o tamanho da string, p = pular de quanto e quanto pular)
# Pegando print(nome[0:len(nome):2]) fica:
print(nome[0: 14: 2])
'''CloCsoi (C e l s o C u s t o d i o pulou de 2 em 2. E 14 é o tamanho da String)'''

# :: == tudo e ::-1 é tudo ao contrário
print(nome[::])
'''Celso Custodio'''
print(nome[::-1])
'''oidotsuC osleC'''