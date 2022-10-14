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
cursor.execute('CREATE TABLE categorias (id_categorias INTEGER PRIMARY KEY AUTOINCREMENT, nome_categoria VARCHAR(100));')
cursor.execute('CREATE TABLE tarefas(id_tarefas INTEGER PRIMARY KEY AUTOINCREMENT, nome_tarefa VARCHAR(100), status_tarefa VARCHAR(100), id_categorias INT NOT NULL, FOREIGN KEY(id_categorias) REFERENCES categorias(id_tarefas));')
cursor.execute('ALTER TABLE categorias RENAME TO categorias_TODO')
print(f'{"ESCOLHA UMA DAS OPÇÕES ABAIXO":^40}')
print('*'*40)
opcao = int(input('[1]- INSERIR NOVOS VALORES.\n[2]- ATUALIZAR DADOS.\n[3]- EXCLUIR.\n>>>> '))
print('-='*20)
    
if opcao == 1:
    tabela = int(input('QUAL TABELA DESEJA INSERIR NOVOS VALORES?\n>>> [1] CATEGORIAS ou [2] TAREFAS <<<\n>>> '))

    if tabela == 1:
        nome_categoria = str(input('DIGITE A NOVA CATEGORIA:\n'))
        valores = [nome_categoria]
        inserir = 'INSERT INTO categorias(nome_categoria) VALUES(?)'
        cursor.execute(inserir, valores)

    #cursor.execute('INSERT INTO categorias(nome_categoria) VALUES("Trabalho"), ("Familia"), ("Faculdade"), ("Casa");')

    elif tabela == 2:
        nome_tarefa = str(input('DIGITE A NOVA TAREFA:\n'))
        status = str(input('DIGITE O STATUS DA TAREFA:\n>>> '))
        categoria_id = str(input('DIGITE O ID DA CATEGORIA:\nTRABALHO = 1 / FAMILIA = 2 / FACULDADE = 3 / CASA = 4\nIGREJA = 5 / VIAJEM = 6 / CURSO DE INGLÊS = 7\n>>> '))
        valores = [nome_tarefa, status, categoria_id]
        inserir = 'INSERT INTO tarefas(nome_tarefa, status_tarefa, id_categorias) VALUES(?, ?, ?)'
        cursor.execute(inserir, valores)

elif opcao == 2:
    escolha_tabela = int(input('QUAL TABELA DESEJA ATUALIZAR?\nCATEGORIAS = 1\nTAREFAS = 2\n>>>'))
    print('-'*30)

    if escolha_tabela == 1:
        id = int(input('DIGITE O ID REFERENTE AO VALOR A SER ATUALIZADO:\n>>> '))
        nome_cat_atua = input('DIGITE O NOME ATUALIZADO:\n>>> ')
        valores = [nome_cat_atua, id]
        atualizacao = 'UPDATE categorias SET nome_categoria = (?) where id_categorias= (?)'
        cursor.execute(atualizacao, valores)

    if escolha_tabela == 2:
        coluna = int(input('QUAL COLUNA DESEJA ATUALIZAR?\nNOME = 1\nSTATUS = 2\nID CATEGORIA = 3\n>>> '))
        print('-'*30)

        if coluna == 1:
            id_tarefa = int(input('DIGITE O ID REFERENTE AO VALOR A SER ATUALIZADO:\n>>> '))
            nome_tarefa_atualizado = input('DIGITE NOME ATUALIZADO:\n>>> ')
            valores = [nome_tarefa_atualizado, id_tarefa]
            atualizacao = 'UPDATE tarefas SET nome_tarefa = (?) where id_tarefas= (?)' 
            cursor.execute(atualizacao, valores)

        elif coluna == 2:
            id_status = int(input('DIGITE O ID REFERENTE AO STATUS A SER ATUALIZADO:\n>>> '))
            status_tarefa_atualizado = input('DIGITE NOME ATUALIZADO:\n>>> ')
            valores = [status_tarefa_atualizado, id_status]
            atualizacao = 'UPDATE tarefas SET status_tarefa = (?) where id_tarefas= (?)' 
            cursor.execute(atualizacao, valores)

        elif coluna == 3:
            id_status = int(input('DIGITE O ID REFERENTE AO VALOR A SER ATUALIZADO:\n>>> '))
            id_cat_atua = int(input('DIGITE O NOVO ID_CATEGORIA:\n>>> '))
            valores = [id_cat_atua, id_status]
            atualizacao = 'UPDATE tarefas SET id_categorias = (?) where id_tarefas= (?)' 
            cursor.execute(atualizacao, valores)

    elif opcao == 3:
        exclusao = int(input('QUAL TABELA DESEJA EXCLUIR?\n1- CATEGORIAS\n2- TAREFAS\n>>> '))
        print('-'*30)
        if exclusao == 1:
            cursor.execute('DROP TABLE categorias')
        elif exclusao == 2:
            cursor.execute('DROP TABLE tarefas')

conexao.commit()
conexao.close()