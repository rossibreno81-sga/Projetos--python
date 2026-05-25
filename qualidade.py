#Multiplas Funções--Exercicio controle de qualidade
def cabecalho():
    print("\n" + "=" * 30)
    print("SISTEMA DE QUALIDADE")
def verificar_status(peso):
    if peso >= 50 and peso <= 100:
       return "Aprovada"
    else:
       return "Reprovada"
cabecalho()
peso_item = float(input("Digite o peso do item em gramas: "))
status = verificar_status(peso_item)
print(f"Resultado de Inspeção:{status}")
print("=" * 30)