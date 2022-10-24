#Criei um programa que possua as variáveis A, B e C. 
# Imprima o resultado de A + B caso ele seja menor do que C, caso contrário imprima que o valor é menor. 
# Teste a aplicação com alguns valores nas variáveis sugeridas.

def retorno():

    A = int(input("informe um número para A: "))
    B = int(input("informe um número para B: "))
    C = int(input("informe um número para C: "))


    if (A + B < C):
        print("o resultado é Menor que",C)
        return True

    else:
        print("O resultado é Maior que",C)
        return False
print(retorno())
