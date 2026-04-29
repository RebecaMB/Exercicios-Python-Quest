senha= int(input("Digite a senha para acessar o sistema: "))
senha_cadastrada = 1234
if senha == senha_cadastrada:
    print("Acesso liberado")
elif senha != senha_cadastrada:
    print ("Acesso negado")
elif senha == " ":
    print("Senha inválida")