def calcula_pizza(tamanho, qtd):
    if tamanho == 'pequena':
        preco = 20
    elif tamanho == 'média':
        preco = 30
    else:
        preco = 50
    
    if qtd == 1:
        preco = preco + 5
    elif qtd == 2:
        preco = preco + 10
    else:
        preco = preco + 15

    return f'Tamanho: {tamanho}, Sabores: {qtd}. Preco total R${preco:.2f}'

tam = input('Tamanho: ')
qtdade = int(input('Sabores: '))

print(calcula_pizza(tam, qtdade))
