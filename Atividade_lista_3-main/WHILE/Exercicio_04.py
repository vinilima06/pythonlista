# Função para obter um número do usuário e garantir que seja um número válido
def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# Obtendo dois números do usuário
numero1 = obter_numero("Digite o primeiro número: ")
numero2 = obter_numero("Digite o segundo número: ")

# Listas para armazenar os resultados das somas
resultados = []

# Realizando 3 somas diferentes e armazenando os resultados
for i in range(3):
    resultado = numero1 + numero2
    resultados.append(resultado)
    print(f"Soma {i + 1}: {resultado}")

# Calculando o totalizador das 3 somas
totalizador = sum(resultados)

# Exibindo o totalizador final
print(f"\nTotalizador das 3 somas: {totalizador}")