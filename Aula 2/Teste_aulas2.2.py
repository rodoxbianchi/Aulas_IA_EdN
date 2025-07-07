# Conversor de Cambio
valor_em_reais = float(input("Digite o valor em R$: "))

taxa_dolar = 5.49
taxa_euro = 6.31

valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

print(f"R$ {valor_em_reais:.2f} equivale a: ")
print(f"$ {valor_em_dolares:.2f} dolares")
print(f"€ {valor_em_euros:.2f} euros")