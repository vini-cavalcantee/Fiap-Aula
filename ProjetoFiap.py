# Função para classificar o nível de satisfação
def classificar_satisfacao(nota):
    if nota >= 90:
        return "Atendimento de qualidade"
    elif 70 <= nota <= 89:
        return "Atendimento neutro"
    else:
        return "Atendimento insatisfatório"

# Solicitar a nota de satisfação ao usuário
nota = float(input("Digite a nota de satisfação (0 a 100): "))

# Verificar se a nota está dentro do intervalo válido
if 0 <= nota <= 100:
    # Imprimir a classificação do atendimento
    print(classificar_satisfacao(nota))
else:
    print("Nota inválida. A nota deve estar entre 0 e 100.")
    