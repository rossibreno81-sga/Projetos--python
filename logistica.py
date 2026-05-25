#Calculadora de frete--Sistema de Logistica--
def calcular_frete(peso):
    if peso <= 20:
        valor = peso * 10
        print("Carga leve")
    else:
        valor = peso * 15 + 20 #taxa extra
        print("carga pesada")
    return valor

 peso_carga = float(input("Digite o peso da carga em kg:"))
 frete = calcular_frete(peso_carga)
 print(f"O valor final do frete é: R${frete:.2f}")


#Breno Nadal Rossi