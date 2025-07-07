def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    - valor_conta (float): O valor total da conta.
    - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%).

    Retorna:
    - float: O valor da gorjeta calculada.
    """
    gorjeta = (porcentagem_gorjeta / 100) * valor_conta
    return gorjeta


valor = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem de gorjeta desejada (%): "))

valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"O valor da gorjeta é: R$ {valor_gorjeta:.2f}")