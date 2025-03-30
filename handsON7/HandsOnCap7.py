import json

with open ('C:\\Users\\vinic\\Desktop\\MeuProjeto\\enriched.json', 'r', encoding='utf8') as file:
    dados = json.load(file)

male_count = 0
female_count = 0
nogender_count = 0

for person in dados.get('people', []):
    nome = person.get('name', [])
    genero = person.get('gender', [])
    print(f'Nome: {nome}, Genero: {genero}')

    if genero == 'male':
        male_count += 1
    elif genero == 'female':
        female_count += 1
    else:  
        nogender_count += 1

print('------------------------------------------------')
print(f'Números de gêneros Masculino: {male_count}')
print(f'Números de gêneros Female: {female_count}')
print(f'Números de personagens sem genêros: {nogender_count}')