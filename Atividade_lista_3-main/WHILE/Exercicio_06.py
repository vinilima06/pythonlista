def main():
    # Cabeçalho das colunas
    print("Número\tQuadrado\tCubo")
    
    # Inicialização do contador
    num = 0
    
    # Loop WHILE para calcular quadrados e cubos
    while num <= 50:
        quadrado = num ** 2
        cubo = num ** 3
        
        # Impressão dos resultados com tabulação
        print(f"{num}\t{quadrado}\t\t{cubo}")
        
        # Incremento do contador
        num += 1

if __name__ == "__main__":
    main()
    