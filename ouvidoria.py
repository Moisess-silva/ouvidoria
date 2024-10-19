from operacoesbd import *

opcao = 1

conn= criarConexao("localhost","root","12345","ouvidoria_ads")

while opcao != 5:
    print("\n1) Listagem das manifestações \n2) Adicionar uma nova Manifestação \n3) Pesquisar uma manifestação por código \n4) Excluir uma manifestação pelo pelo código \n5)Sair do Sistema")
    opcao= int(input("Digite a opção desejada: "))

    if opcao == 1: #listagem de manifestações
        consultaReclamacao = "select * from Reclamacao"
        reclamacao = listarBancoDados(conn, consultaReclamacao)

        if len(reclamacao)> 0:

            print("\nlista de Reclamações")
            for item in reclamacao:
                print("- Codigo", item[0], "\nTitulo:", item[1], ",", "Autor:", item[2])
        else:
            print("Não possui reclamações registradas!")

        consultaElogio = "select * from Elogio"
        elogio = listarBancoDados(conn, consultaElogio)

        print("\nlista de Elogios:")
        if len(elogio)> 0:
            for item in elogio:
                print("- Codigo", item[0], "\nTitulo:", item[1], ",", "Autor:", item[2])
        else:
            print("Não possui elogios registrados!")
        consultaSugestao = "select * from Sugestao"

        sugestao = listarBancoDados(conn, consultaSugestao)
        print("\nlista de Sugestões: ")
        if len(sugestao)> 0:
            for item in sugestao:
                print("- Codigo", item[0], "\nTitulo:", item[1], ",", "Autor:", item[2])
        else:
            print("Não possui sugestões registradas!")


    elif opcao == 2: #adicionar
       print("1)Reclamação \n2)Elogio \n3)Sugestão")
       opcaoEscolhida= int(input("digite a opcão que deseja adicionar: "))

       if opcaoEscolhida == 1:
           tituloDaManifestacao = input("qual é a reclamação que deseja fazer? ")
           autorDaManifestacao = input("qual é o seu nome? ")

           consultaAdicionarReclamacao = "insert into Reclamacao(titulo,autor) values(%s,%s)"
           dados = [tituloDaManifestacao, autorDaManifestacao]

           insertNoBancoDados(conn, consultaAdicionarReclamacao, dados)

       elif opcaoEscolhida == 2:
           tituloDaManifestacao = input("qual é o elogio que deseja fazer? ")
           autorDaManifestacao = input("qual é o seu nome? ")

           consultaAdicionarElogio = " insert into Elogio(titulo,autor) values(%s,%s)"
           dados = [tituloDaManifestacao, autorDaManifestacao]

           insertNoBancoDados(conn, consultaAdicionarElogio, dados)

       elif opcaoEscolhida == 3:
           tituloDaManifestacao = input("qual é a sugestão que deseja fazer? ")
           autorDaManifestacao = input("qual é o seu nome?")

           consultaAdicionarSugestao = "insert into Sugestao(titulo,autor) values(%s,%s)"
           dados = [tituloDaManifestacao, autorDaManifestacao]

           insertNoBancoDados(conn, consultaAdicionarSugestao, dados)
       else:
           print("Opção Inválida!")

    elif opcao ==3:
        print("pesquisar")

    elif opcao ==4:
        print("1)Reclamação \n2)Elogio \n3)Sugestão")
        opcao = int(input("digite a sua opção: "))

        if opcao == 1:

            opcaoExcluir = int(input("qual a reclamação que voce deseja excluir? "))
            consultaExcluirBd = "delete from Reclamacao where codigo = %s"
            dados = [opcaoExcluir]

            remocao = excluirBancoDados(conn, consultaExcluirBd, dados)

            if remocao > 0:
                print("reclamação excluida com sucesso!")
            else:
                print("não possui reclamação nesta posição para remover!")

        elif opcao == 2:

            opcaoExcluir = int(input("qual a elogio voce deseja excluir? "))
            consultaExcluirBd = "delete from Elogio where codigo = %s"
            dados = [opcaoExcluir]

            remocao = excluirBancoDados(conn, consultaExcluirBd, dados)

            if remocao > 0:
                print("elogio excluido com sucesso!")
            else:
                print("não possui elogios nesta posição para remover!")

        elif opcao == 3:

            opcaoExcluir = int(input("qual a sugestão voce deseja excluir? "))
            consultaExcluirBd = "delete from Sugestao where codigo = %s"
            dados = [opcaoExcluir]

            remocao = excluirBancoDados(conn, consultaExcluirBd, dados)

            if remocao > 0:
                print("sugestão excluida com sucesso!")
            else:
                print("não possui sugestão nesta posição para remover!")
        else:
            print("Opção Inválida!")

    elif opcao !=5:
        print("Opção Inválida!")



encerrarConexao(conn)
print("obrigado por fazer o seu registro!" )

