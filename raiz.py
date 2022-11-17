import math

print('\033[1;33;40mdescubra a raiz quadrada, seguindo abaixo \033[m')
n1 = int(input('digite um número inteiro "para a raiz": '))
raiz = math.sqrt(n1)
print(f'\033[1;32;40ma raiz quadrada de {n1}, é\033[m: \033[4;31;40m{raiz}\033[m')
