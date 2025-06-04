import os
email=input("Digite o seu usuário de email (antes do @): ")
tam=len(email)
while(tam<=5):
    email=input("Informe um usuário com mais de 5 caracteres: ")
    tam=len(email)
print("1.@estudantes.ifpr.edu.br")
print("2.@gmail.com")
print("3.@hotmail.com")
print("4.outro")
opcao=0
while(opcao<1 or opcao>4):
    opcao=int(input("OPÇÃO: "))
    if(opcao==1):
        arroba="@estudantes.ifpr.edu.br"
    elif(opcao==2):
        arroba="@gmail.com"
    elif(opcao==3):
        arroba="@hotmail.com"
    elif(opcao==4):
        arroba=input("Informe o usuário após o @: ")
        while(not("@" in arroba and ".com" in arroba)):
            arroba=input("O usuário informado precisa conter '@' e '.com': ")
print(f"{email}{arroba}")
confirmacao=input("O seu email está correto (S ou N)? ")
if(confirmacao=="N"):
    exit
msgcommit=input("Digite sua mensagem do commit: ")
tamcommit=len(msgcommit)
while(tamcommit<=10):
    msgcommit=input("Detalhe mais a sua mensagem: ")
    tamcomit=len(msgcommit)

# Configurar o email
c=(f"git config user.email \"{email}\"")
os.system(c)

# Identificar as novidades e incluir no commit
c=(f"git add *")
os.system(c)

# Registrar o commit com uma mensagem
c=(f"git commit -m \"{msgcommit}\"")
os.system(c)

# Enviar para os servidores do github
c=(f"git push")
os.system(c)