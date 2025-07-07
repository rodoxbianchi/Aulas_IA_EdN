def analisar_numeros():
    numeros = []
    pares = 0
    impares = 0

    print("Digite os números que deseja analisar.")
    print("Para encerrar, digite 'sair'.\n")

    while True:
        entrada = input("Digite um número: ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'sair' para encerrar.")

    print("\nAnálise concluída:")
    print(f"Total de números digitados: {len(numeros)}")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

# Executa o programa
analisar_numeros()