x = 0
y = int
while x != 1:

    y = input("Digite a senha ")

    if y == "1234":
        print("Bem vindo!")
        x = 1
    else:
        print("Senha incorreta, tente novamente")