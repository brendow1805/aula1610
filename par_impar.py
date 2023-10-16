# Sistema que verifica se um número informado é par ou ímpar

#Apresentação

print('\n\t\t\t -- Verificador de Num. Par ou Impar -- ')

#Entrada
num = int(input('Informe um número: '))

#Processamento e saída

if num % 2 == 0:
    print(f'{num} é par!')
else:
    print(f'{num} é impar!')
