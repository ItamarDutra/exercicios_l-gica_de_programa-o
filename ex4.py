from pprint import pprint

print("====================================")
print("===========MENU PRINCIPAL===========")

id = 1
biblioteca = []

def cadastrar (id):
    print(f"ID do livro: {id}")
    livro = {
        "id": id,
        "nome": input("nome: "),
        "autor": input("autor: "),
        "editora": input("editora: ")
        }
    biblioteca.append(livro)

def remover_livro (): 
    id_del = int(input("Digite o ID do livro a ser removido: "))
    for iten in biblioteca:
        if iten["id"] == id_del:
            biblioteca.remove(iten)
            print('Livro Removido.')

resp = ""
while resp != "4":
    print("1) Cadastrar Livro\n2) Consultar Livro\n3) Remover Livro\n4) Encerrar Programa")
    resp = input(">>> ")
    if resp == "1": 
        cadastrar(id)
        id += 1
    elif resp == "2":
        consult_resp = True
        while consult_resp != "4":
            print('''1. Consultar Todos  
2. Consultar por Id 
3. Consultar por Autor 
4. Retornar ao menu ''')
            consult_resp = input(">>> ")
            if consult_resp == "1":
                for itens in biblioteca:
                    print("-------------------------")
                    print(f"ID: {itens["id"]} \nNome: {itens["nome"]} \nAutor: {itens["autor"]} \nEditora: {itens["editora"]}\n")
            elif consult_resp == "2":
                id_cons = int(input("informe o id do livro a ser consultado: "))
                for itens in biblioteca:
                    if itens["id"] == id_cons:
                        print("-------------------------")
                        print(f"ID: {itens["id"]} \nNome: {itens["nome"]} \nAutor: {itens["autor"]} \nEditora: {itens["editora"]}\n")
            elif consult_resp == "3":
                autor_cons = input("informe o Autor dos livros a serem consultados: ")
                for itens in biblioteca:
                    if itens["autor"] == autor_cons:
                        print("-------------------------")
                        print(f"ID: {itens["id"]} \nNome: {itens["nome"]} \nAutor: {itens["autor"]} \nEditora: {itens["editora"]}\n")
            else:
                continue
        print("-------------------------")

    elif resp == "3":
        remover_livro()
     
    else:
        continue