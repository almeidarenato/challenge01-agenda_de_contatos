
from funcoes_contatos import adicionar_contato,apagar_contato,editar_contato,favoritar_contato,ver_contatos
lista_de_contatos = []

while True:
    print("\n Agenda de Contatos")
    print("1. Adicionar contato")
    print("2. Ver Contatos")
    print("3. Editar Contato")
    print("4. Favoritar Contato")
    print("5. Deletar Contato")
    print("6. Sair")
    escolha = input("Digite a sua opção: ")
    match escolha: 
         case "1":
              nome_contato = input("Digite o nome do Contato :")
              telefone_contato = input("Digite o telefone do Contato :")
              email_contato = input("Digite o e-mail do Contato :")
              contato = {"nome":nome_contato,"telefone":telefone_contato,"email":email_contato,"favorito":False}
              adicionar_contato(lista_de_contatos=lista_de_contatos,contato=contato)
         case "2":
              ver_contatos(lista_de_contatos)
         case "3":
              ver_contatos(lista_de_contatos)
              indice_contato = input("Digite o número do contato que deseja atualizar: ")
              nome_contato = input("Digite o nome do Contato")
              telefone_contato = input("Digite o telefone do Contato")
              email_contato = input("Digite o e-mail do Contato")
              contato = {"nome":nome_contato,"telefone":telefone_contato,"email":email_contato}
              editar_contato(lista_de_contatos=lista_de_contatos, indice_contato= indice_contato,contato=contato)
         case "4":
               ver_contatos(lista_de_contatos)
               indice_contato = input("Digite o número do contato que deseja favoritar: ")
               favoritar_contato(lista_de_contatos=lista_de_contatos,indice_contato=indice_contato)
         case "5":
              ver_contatos(lista_de_contatos)
              indice_atividade = input("Digite o número da atividade que deseja deletar: ")
              apagar_contato(lista_de_contatos=lista_de_contatos,indice_atividade=indice_atividade)
         case "6":
              break