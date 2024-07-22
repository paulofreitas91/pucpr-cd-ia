# 3. Crie um algoritmo de autenticação baseado em usuário e senha 

usuario_correto = "admin"
senha_correta = "admin"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
  print("Usuário autenticado")
else:
  print("Usuário ou senha incorretos")
