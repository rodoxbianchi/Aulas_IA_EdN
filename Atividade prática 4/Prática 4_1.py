def calculadora():
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
   
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite apenas números válidos.")
        return

    
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Erro: divisão por zero não é permitida.")
            return
        resultado = num1 / num2
    else:
        print("Operação inválida.")
        return

    
    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")


calculadora()


 