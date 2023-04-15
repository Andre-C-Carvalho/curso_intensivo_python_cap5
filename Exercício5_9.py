lista_usuarios = ["rafael", "lucas", "eduardo", "joana", "admin"]
# lista_usuarios = [] 
lista_teste = ["rafael", "lucas", "eduardo", "joana", "admin", "ricardo"]

if lista_usuarios:
    for user in lista_teste:
        print("O usuário é: " + user)
        if user in lista_usuarios:
            if user == "admin":
                print("Olá Admin, gostaria de ver um relatório de status?\n")
            else:
                print("Olá " + user.title() + ", obrigado por fazer login novamente.\n")
        else:
            print("O usuário não existe.")
else:
    print("Não existem usuários ativos")
