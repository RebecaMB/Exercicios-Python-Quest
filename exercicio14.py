visualizacoes = int (input("Digite o número de visualizações do vídeo: "))
numero_de_visualizacoes = visualizacoes
if numero_de_visualizacoes <= 10000:
    print ("Não há monetização")
elif numero_de_visualizacoes <= 100000:
    valor_total = numero_de_visualizacoes * 0.02 
elif numero_de_visualizacoes <= 1000000:
    valor_total = numero_de_visualizacoes * 0.03
else:
   valor_total = numero_de_visualizacoes * 0.05
if numero_de_visualizacoes > 500000:
    valor_total = valor_total + 500
print("Valor total da monetização a ser recebida:  ", valor_total)
