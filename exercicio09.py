altura = float(input("Digite sua altura: "))
sexo = str(input("Digite seu sexo: "))
if sexo == "Masculino":
    peso = (72.7 * altura) - 58
    print("Peso ideal: ", peso)
elif sexo == "Feminino":
    peso = (62.1 * altura) - 44.7
    print("Peso ideal: ", peso)