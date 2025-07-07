idade = int(input("Digite sua idade: "))

if idade <= 0:
    print("Idade inválida. Digite uma idade válida:")
elif idade <=13:
    print("Você é menor de idade.")
elif idade <= 17:
    print("Você é um adolescente!")
elif idade <=59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")