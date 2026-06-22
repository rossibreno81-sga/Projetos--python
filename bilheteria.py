#aluno1: formato do novo filme
def formatar(nome):
    return nome.upper()
#aluno2: verificação de acesso
def verificador(idade):
    if idade >=18:
     return "Autorizado"
    else:
       return "Não Autorizado"
#aluno3: mensagem de roteiro
def gerar_mensagem(status)
   if status == "Autorizado"
      return "Tenha uma ótima sessão"
   else:
      return "Sinto muito, idade não autorizada"
#aluno4: integrador do projeto
nome_filme = input("Digite o nome do filme:")
idade_filme = int(input("Digite sua idade:"))
filme = formatar(nome_filme)
status_final = verificador(idade_filme)
mensagem = gerar_mensagem(status_final)
print(f"\nFilme:{filme}")
print(f"status:{status_final}}")
print(f"aviso:{mensagem}")