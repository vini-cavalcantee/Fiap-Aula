'''soma = 0
alimentos = int(input('Quantos alimentos você comeu hoje? '))

for x in range(1, alimentos + 1):
    caloria = float(input(f'informe as calorias do {x}° alimento: '))
    soma = soma + caloria

print('Total de calorias do dia: ', soma)'''

nota_impar = 0
nota_par = 0
for x in range(1, 51, 2):
    print('Você está digitando os alunos da nota IMPAR!!')
    nota = float(input(f'Nota do {x}° Aluno: '))
    nota_impar = nota_impar + nota

for x in range(0, 51, 2):
    print('Você está digitando os alunos da nota PAR!!')
    nota = float(input(f'Nota do {x}° Aluno: '))
    nota_par = nota_par + nota

media_impar = nota_impar / 25
media_par = nota_par / 25

print('Média dos Alunos Ímpares: ', media_impar)
print('Média dos Alunos Pares: ', media_par)

if media_par > media_impar:
    print('Os Alunos Pares tiveram o melhor desempenho!')
else:
    print('Os Alunos Impares tiveram o melhor desempenho!')