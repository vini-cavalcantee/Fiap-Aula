

class NumerosNegativos (Exception):
    def __str__(self):
        return 'ERRO! Você forneceu números negativos'

try:
    vltotoal = float(input('Valor total das compras: R$'))
    qtitens = int(input('Quantidade de itens comprados: '))
    
    if vltotoal < 0 or qtitens < 0:
        raise NumerosNegativos
    
    media = round(vltotoal / qtitens)

except ZeroDivisionError:
    print('Erro! Não é possível realizar divisões por zero!')

except ValueError:
    print('ERRO! Entre com números válidos!')

except NumerosNegativos as error:
    print(error)

else:
    print('Média das compras: ', media)

finally:
    print('OBRIGADO')