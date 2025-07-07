def calcular_preco_final(preco_original: float, percentual_desconto: float) -> float:
    """
    Calcula o preço final após aplicar o desconto percentual.

    :param preco_original: preço original do produto
    :param percentual_desconto: porcentagem de desconto (ex: 20 para 20%)
    :return: preço final arredondado para 2 casas decimais
    """
    valor_desconto = (percentual_desconto / 100) * preco_original
    preco_final = preco_original - valor_desconto
    return round(preco_final, 2)

def main():
    try:
        preco = float(input("Digite o preço original do produto: R$ "))
        desconto = float(input("Digite o percentual de desconto (%): "))
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
        return

    preco_com_desconto = calcular_preco_final(preco, desconto)
    print(f"O preço final após desconto é: R$ {preco_com_desconto:.2f}")

if __name__ == "__main__":
    main()