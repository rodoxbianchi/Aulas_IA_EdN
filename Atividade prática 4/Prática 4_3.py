def verificar_senha(senha):

    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."


    if not any(char.isdigit() for char in senha):
        return "A senha deve conter pelo menos um número."

    return "Senha válida!"


senha = input("Digite uma senha: ")
resultado = verificar_senha(senha)
print(resultado)