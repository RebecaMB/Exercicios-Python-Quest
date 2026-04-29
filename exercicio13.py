conta= int (input("Digite 1 para conta comum ou digite 2 para conta premium: "))
conta_comum = 1
conta_premium = 2
saldo_medio = float(input("Digite o saldo médio mensal da sua conta: "))
if conta == conta_comum and saldo_medio < 1000:
    print("Tarifa de 25 reais")
elif conta == conta_comum and saldo_medio <= 5000:
    print("Tarifa de 15 reais")
elif conta == conta_comum and saldo_medio > 5000:
    print("Isento")
if conta == conta_premium and saldo_medio < 5000: 
    print("Tarifa de 20 reais")
elif conta == conta_premium and saldo_medio >= 5000:
    print("Isento")