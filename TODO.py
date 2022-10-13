'''Para este módulo, vamos modelar um banco de dados de aplicação TODO usando SQLite. 

Com esta base de dados, vamos criar a aplicação CLI TODO com as funcionalidades:

Criar, atualizar e excluir um TODO;
Criar, atualizar e excluir categorias;
Listar todos os afazeres de um dia específico;
Listar todas as categorias;
Marcar uma tarefa como concluída.
Para esta atividade, recomenda-se criar o banco de dados e as tabelas utilizando o DBeaver e,
para cada item da atividade, fazer um programa Python nos moldes dos programas criados nesta semana.'''


import sqlite3

conexao = sqlite3.connect('exercicio_TODO')
cursor = conexao.cursor()
#cursor.execute('CREATE TABLE categorias (id_categorias INTEGER PRIMARY KEY AUTOINCREMENT, nome_categoria VARCHAR(100));')
opcao = int(input('1- EXCLUIR TABELA\n2- ATUALIZAR O NOME DA TABELA\n3- CRIAR TABELA TAREFAS\n4- INSERIR COLUNAS NA TABELA CATEGORIAS\n5- INSERIR TAREFAS\n6- COLUNA'))
print('-='*15)
if opcao == 1:
    exclusao = int(input('QUAL TABELA DESEJA EXCLUIR?\n1- CATEGORIAS\n2- TAREFAS'))
    if exclusao == 1:
        cursor.execute('DROP TABLE categorias_TODO')
    else:
        cursor.execute('DROP TABLE tarefas')

elif opcao == 2:
    cursor.execute('ALTER TABLE categorias RENAME TO categorias_TODO')

elif opcao == 3:
    colunas1 = []
    nome_tabela = input('DIGITE O NOME DA TABELA QUE VOCÊ DESEJA CRIAR:\n')
    quant_colunas = int(input(f'DIGITE A QUANTIDADE DE COLUNAS QUE DESEJA CRIAR NA TABELA\n'))
    for coluna in range(quant_colunas):
        colunas1.append(input(f'Digite o nome da {coluna+1}º coluna'))
    colunas= [nome_tabela, colunas1]
    inseri = "CREATE TABLE (?)((?) INTEGER PRIMARY KEY AUTOINCREMENT,(?) VARCHAR(100));"
    cursor.execute(inseri, colunas)

elif opcao == 4:
    nome_categoria = str(input('Digite a categoria:\n'))
    valores = [nome_categoria]
    inserir = 'INSERT INTO categorias(nome_categoria) VALUES(?)'
    cursor.execute(inserir, valores)

    #cursor.execute('INSERT INTO categorias(nome_categoria) VALUES("Trabalho"), ("Familia"), ("Faculdade"), ("Casa");')

elif opcao == 5:
    nome_tarefa = str(input('Digite a tarefa:\n'))
    status = str(input('Digite o status da tarefa:\n'))
    categoria_id = str(input('Digite o ID da categoria:\nTRABALHO = 1\nFAMILIA = 2\nFACULDADE = 3\nCASA = 4\n'))
    valores = [nome_tarefa, status, categoria_id]
    inserir = 'INSERT INTO tarefas(nome_tarefa, status_tarefa, id_categorias) VALUES(?, ?, ?)'
    cursor.execute(inserir, valores)

elif opcao == 6:
    escolha_tabela = int(input('QUAL TABELA DESEJA ATUALIZAR?\nCATEGORIAS = 1\nTAREFAS = 2\n'))
    if escolha_tabela == 1:
        nome_cat_atua = input('Digite nome atualizado:\n')
        id = int(input('Digite o ID referente ao valor a ser atualizado:\n'))
        valores = [nome_cat_atua, id]
        atualizacao = 'UPDATE categorias SET nome_categoria = (?) where id_categorias= (?)'
        cursor.execute(atualizacao, valores)

    if escolha_tabela == 2:
        coluna = int(input('Qual coluna quer atualizar?\nNOME = 1\nSTATUS = 2\nID CATEGORIA = 3\n'))
        if coluna == 1:
            id_tarefa = int(input('Digite o ID referente ao valor a ser atualizado:\n'))
            nome_tarefa_atualizado = input('Digite nome atualizado:\n')
            valores = [nome_tarefa_atualizado, id_tarefa]
            atualizacao = 'UPDATE tarefas SET nome_tarefa = (?) where id_tarefas= (?)' 
            cursor.execute(atualizacao, valores)

        elif coluna == 2:
            id_status = int(input('Digite o ID referente ao status que será atualizado:\n'))
            status_tarefa_atualizado = input('Digite o status atualizado:\n')
            valores = [status_tarefa_atualizado, id_status]
            atualizacao = 'UPDATE tarefas SET status_tarefa = (?) where id_tarefas= (?)' 
            cursor.execute(atualizacao, valores)

        else:
            id_status = int(input('Digite o ID referente ao status que será atualizado:\n'))
            id_cat_atua = int(input('Digite o novo ID_CATEGORIA atualizado:\n'))
            valores = [id_cat_atua, id_status]
            atualizacao = 'UPDATE tarefas SET id_categorias = (?) where id_tarefas= (?)' 
            cursor.execute(atualizacao, valores)



conexao.commit()
conexao.close()