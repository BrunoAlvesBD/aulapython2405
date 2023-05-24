# dado um número inteiro ache a soma de todos os multiplos de 3 e 5.
# Se o número for negativado ou 0 a função deve retornar 0


def multiple(numero):
  contador = 0
  
  if numero <= 0:
    return 0

  for val in range(0, numero+1, 3):
    contador += val
    print(3, val , contador)
  print("-----------------")
  for val in range(0, numero+1, 5):
    if val % 3 == 0:
      continue
    contador += val
    print(5, val, contador)

  return contador 
# print(multiple(3))

# ------------------------------------------------
# exercicio: crie uma lista com os indices dos 2 numeros que somados deem o número de entrada

def indices(lista: list, target: int) -> list:

  for idx, item1 in enumerate(lista):
    for jdx, item2 in enumerate(lista):
      if idx == jdx:
        continue
      if item1 + item2 == target:
        return [idx, jdx]

# print(indices([1, 2, 3], 4))
# -----------------------------------------
# exemplo TP 3.12

"""este método é utilizado para um jogo matemático onde um dígito numérico, uma letra e outro dígito numérico são a entrada. Se a letra for maiúscula, deve-se subtrair o primeiro dígito do segundo. Se a letra for minúscula, deve-se somar ambos os dígitos e se os DÍGITOS forem iguais, deve-se desconsiderar a letra e mostrar o produto entre os dois dígitos.

param entrada: sequencia de três algarismos compostos por número, letra e número

type entrada: str

return: inteiro segundo as regras do jogo.
"""

def jogo_matematico(entrada: str) -> int:
  letra = entrada[1]

  if entrada[0] == entrada[2]:
    return int(entrada[0]) * int(entrada[2])
  elif letra == letra.upper():
    return int(entrada[2]) - int(entrada[0])
  else:
    return int(entrada[0]) + int(entrada[2])

print(jogo_matematico('3A3'))