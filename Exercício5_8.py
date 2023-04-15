lista_usuarios = ["rafael", "lucas", "eduardo", "joana", "admin"]
lista_teste = ["rafael", "lucas", "eduardo", "joana", "admin", "ricardo"]


for user in lista_teste:
    print("O usuário é: " + user)
    if user in lista_usuarios:
        if user == "admin":
            print("Olá Admin, gostaria de ver um relatório de status?\n")
        else:
            print("Olá " + user.title() + ", obrigado por fazer login novamente.\n")
    else:
        print("O usuário não existe.")
