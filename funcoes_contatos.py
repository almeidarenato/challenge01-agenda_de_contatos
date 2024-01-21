def adicionar_contato(lista_de_contatos,contato):
    lista_de_contatos.append(contato)
    print("Contato cadastrado com sucesso")
    return
def ver_contatos(lista_de_contatos):
    print("Lista Contatos")
    for indice,contato in enumerate(lista_de_contatos, start=1):
        favorito = "★" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}- [{favorito}] {nome_contato} \ntel: {telefone_contato} email:{email_contato}")
    return 
def editar_contato(lista_de_contatos,indice_contato,contato):
    print("Contatos editado com sucesso")
    return 
def favoritar_contato(lista_de_contatos,indice_contato):
    print("Contato favoritado com sucesso")
    return
def apagar_contato(lista_de_contatos,contato):
    print("Contato apagado com sucesso")
    return
