altura = float (input ("Digite sua altura em metros: "))
peso = float (input ("Digite seu peso em kg: "))
indice_de_massa_corporal = peso / (altura**2)
if indice_de_massa_corporal < 18.5:
    print("Abaixo do peso")
elif indice_de_massa_corporal <= 24.9:
    print("Peso normal")
elif indice_de_massa_corporal <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")