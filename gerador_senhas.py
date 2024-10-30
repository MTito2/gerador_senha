import random
import os

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cacteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/', '|', '\\', '`', '~']
senhas_geradas = [""]

#Função senhas por nível
def gerar_senhas_por_niveis(nivel):
    senha = ""
    
    if nivel == "B":
        for i in range(6):
            senha += random.choice(letras)
    
    elif nivel == "M":
        listas_somadas = letras + numeros
        for i in range(8):
            senha += random.choice(listas_somadas)

    elif nivel == "A":
        listas_somadas = letras + numeros + cacteres_especiais
        for i in range(12):  
            senha += random.choice(listas_somadas)
    
    return senha

#Função senhas customizáveis
def gerar_senhas_customizavel(**kwargs):
    configuracoes = kwargs
    listas_somadas = letras.copy()
    tamanho = configuracoes["tamanho"]
    senha = ""
    
    if configuracoes["incluir_num"] == True:
        listas_somadas += numeros.copy()

    if configuracoes['incluir_especiais'] == True:
        listas_somadas += cacteres_especiais.copy()
    for i in range(tamanho):
        senha += random.choice(listas_somadas)
    
    return senha

#Menu
while True:
    print(70*"-")
    print("Escolha uma opção:")
    print("[1] - Gerar senha por nível\n[2] - Gerar senha customizável\n[3] - Listar senhas\n[4] - Sair")
    op = input("Opção: ")
    os.system("cls")

    if op not in ("1","2","3"):
        print("Opção inválida")
        print()
        continue

    #Menu senhas por nível 
    if op == "1":
        os.system("cls")
        print("[B]ásico\n[M]édio\n[A]vançado")
        nivel = input("Escolha um nível: ").upper()

        if nivel not in ("B","M","A"):
            print("Opção inválida")
            print()
            continue   

        senha = gerar_senhas_por_niveis(nivel)
        if senha in senhas_geradas:
            senha = gerar_senhas_por_niveis(nivel)
        senhas_geradas.append(senha)
        
        print(f"Senha: {senha}")
   
    #Menu senhas customizáveis
    elif op == "2":
        tamanho = input("Informe o tamanho: ")
        os.system("cls")

        if tamanho.isdigit():
            tamanho = int(tamanho)
        else:
            print("É aceito apenas números.")
            continue

        incluir_num = input("Deseja incluir números? [S/N] ").upper()
        os.system("cls")

        if incluir_num not in ("S","N"):
            print("Resposta inválida")
            continue
        if incluir_num == "S":
            incluir_num = True
        else:
            incluir_num = False

        incluir_especiais = input("Deseja incluir caracteres especiais? [S/N] ").upper()
        os.system("cls")

        if incluir_especiais not in ("S","N"):
            print("Resposta inválida")
            continue
        if incluir_especiais == "S":
            incluir_especiais = True
        else:
            incluir_especiais = False
        os.system("cls")
        
        senha = gerar_senhas_customizavel(tamanho=tamanho, incluir_num=incluir_num, incluir_especiais=incluir_especiais)
        if senha in senhas_geradas:
            senha = gerar_senhas_customizavel(tamanho=tamanho, incluir_num=incluir_num, incluir_especiais=incluir_especiais)
        senhas_geradas.append(senha)
        print(f"Senha: {senha}")

    #Menu exibir senhas
    elif op == "3":
        for i, valor in enumerate(senhas_geradas):
            if i > 0:
                print(f"{i} - {valor}")
            if len(senhas_geradas) == 1:
                print("Nada a exibir")
    
    #Sair
    elif op == "4":
        break