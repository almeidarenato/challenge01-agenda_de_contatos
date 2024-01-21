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
    indice = int(indice_contato) -1
    print(len(lista_de_contatos))
    if indice >= 0 and indice< len(lista_de_contatos) :
            lista_de_contatos[indice]["nome"] = contato["nome"]
            lista_de_contatos[indice]["telefone"] = contato["telefone"]
            lista_de_contatos[indice]["email"] = contato["email"]
            print(f"Contato {indice_contato} atualizada para nome:{contato["nome"]} \n telefone:{contato["telefone"]} email: {contato["email"]}")
    else:
            print("Contato inexistente")  
    return 
def favoritar_contato(lista_de_contatos,indice_contato):
    indice = int(indice_contato) -1
    if lista_de_contatos[indice]["favorito"] != True:
        lista_de_contatos[indice]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito")
    else:
         print(f"Contato {indice_contato} já é favorito")
    return
def desfavoritar_contato(lista_de_contatos,indice_contato):
    indice = int(indice_contato) -1
    if lista_de_contatos[indice]["favorito"] != False:
        lista_de_contatos[indice]["favorito"] = False
        print(f"Contato {indice_contato} desfavoritado")
    else:
        print(f"Contato {indice_contato} já não é favorito")
    return
def apagar_contato(lista_de_contatos,indice_contato):
    indice = int(indice_contato)-1
    if indice >= 0 and indice< len(lista_de_contatos):
        for indice_lista,contato in enumerate(lista_de_contatos,start=1):
            if indice_lista == indice:
                lista_de_contatos.remove(contato)
                print(f'Contato {indice_contato} - foi apagado')
                ver_contatos(lista_de_contatos)
                return
    else:
        print("Contato inexistente")
    return
