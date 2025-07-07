import string

def verificar_palindromo(texto: str) -> str:
    # Remove espaços, pontuação e transforma tudo em minúsculo
    texto_limpo = ''.join(
        char.lower() for char in texto if char.isalnum()
    )
    
    # Compara texto limpo com seu reverso
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

# Exemplo de uso
frase = input("Digite uma palavra ou frase: ")
print(verificar_palindromo(frase))