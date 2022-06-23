print("Olá! Seja bem vinde a Oliveira Trade.")
print("Primeiro, faça seu cadastro.")

nomeUser = input("Digite o seu nome completo: ")
cpfUser = int(input("Digite seu CPF: "))
cepUser = int(input("Digite seu CEP: "))
emailUser = input("Digite seu email: ")
telefoneUser = int(input("Digite seu número de telefone, com DDD: "))
senhaUser = input("Digite sua nova senha: ")

if(len(senhaUser) < 6):
                print("Senha curta demais! Por favor, inclua mais caracteres da próxima vez.")
                print("Comece o cadrastro novamente.")
else:
    print("Cadastro completo!")
    print("Por favor, siga para a página de login.")
    

loginUser = input("Digite seu email: ")
loginSenha = input("Digite a senha cadastrada: ")

if(loginUser != emailUser or loginSenha != senhaUser):
  print("Login não encontrado! Tente novamente.")
else:
    print("Login realizado! Bem vinde,",nomeUser)
      
