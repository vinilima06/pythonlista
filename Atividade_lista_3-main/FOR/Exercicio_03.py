# Função para verificar se a nota é válida
def nota_valida(nota):
    try:
        valor = float(nota)
        return 0 <= valor <= 10
    except ValueError:
        return False

# Lista para armazenar as notas
notas = []

print("Digite 4 notas entre 0 e 10:")

# Laço for para capturar as 4 notas
for i in range(4):
    while True:
        nota = input(f"Nota {i + 1}: ")
        if nota_valida(nota):
            notas.append(float(nota))
            break
        else:
            print("Nota inválida. Por favor, insira um valor entre 0 e 10.")

# Calculando a média das notas
media = sum(notas) / len(notas)

# Exibindo a média final
print(f"\nA média final das notas é: {media:.2f}")