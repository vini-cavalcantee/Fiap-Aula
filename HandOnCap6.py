'''nomes_armaduras = ['Mark I', 'Mark II', 'Mark III', 'Mark IV', 'Mark V']

#mostrando todas as armaduras
for n in nomes_armaduras:   
    print(f'Armadura: ', n)

#adicionando uma armadura nova em uma posição específica:
print(f'Posições de 0 a {len(nomes_armaduras)}')
new_armor = str(input('Nome da nova armadura: '))
#código para aceitas apenas posições válidas
while True:
    posicao =  int(input('Índice na nova armadura: '))
    if posicao >= 0 and posicao <= len(nomes_armaduras):
       break
    print(f'Escolha um aposição válida, entre 0 e {len(nomes_armaduras)}')

#Armaduras atualizadas
nomes_armaduras.insert(posicao, new_armor)
print('Armaduras atualizadas:', nomes_armaduras)
'''
#Criando uma tupla com as características das armaduras
caract_armaduras = (
    'Ferro', 'Pequena', 20,
    'Titânio', 'Média', 30,
    'Carbono', 'Grande', 40)

material = str(input('Qual material deseja contar: '))
qtd_carac = len(caract_armaduras)
contagem = 0

for i in range(qtd_carac):
    if caract_armaduras[i][0] == material:
        contagem += 1