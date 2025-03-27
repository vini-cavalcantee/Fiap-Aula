def avalia_nota(nota):
    if nota >= 90:
        print('Avaliação excelente!')
    elif nota < 70:
        print('Avaliação insatisfatória!')
    else:
        print('Avaliação neutra!')
    
try:
    nota = int(input('Digite sua avaliação sobre o atendimento (0 - 100): '))
    avalia_nota(nota)
except ValueError:
    print('Erro na digitação da nota por favor coloque uma nova válida!')