from datetime import datetime

def calcular_dias_vivo(data_nascimento_str):
   
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    data_atual = datetime.now()
    
    
    dias_vivo = (data_atual - data_nascimento).days
    
    return dias_vivo


data_nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
try:
    dias = calcular_dias_vivo(data_nasc)
    if dias < 0:
        print("Data de nascimento não pode ser futura.")
    else:
        print(f"Você está vivo há {dias} dias!")
except ValueError:
    print("Formato de data inválido. Use dd/mm/aaaa.")