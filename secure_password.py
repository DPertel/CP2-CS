import secrets
import string

def gerar_senha(tamanho, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    if not (8 <= tamanho <= 128):
        raise ValueError("O tamanho da senha deve estar entre 8 e 128 caracteres.")

    caracteres = string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Nenhum conjunto de caracteres selecionado.")

    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Tamanho da senha (8 a 128): "))
        usar_maiusculas = input("Incluir maiúsculas? (s/n): ").lower() == 's'
        usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
        usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

        senha = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)

        print("Senha gerada com sucesso. Copie-a com cuidado.")  # Não exibe a senha diretamente

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
