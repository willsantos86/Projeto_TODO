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
opcao = int(input('1- EXCLUIR TABELA\n2- ATUALIZAR O NOME DA TABELA\n3- CRIAR TABELA TAREFAS\n'))
if opcao == 1:
    cursor.execute('DROP TABLE categorias_TODO')
elif opcao == 2:
    cursor.execute('ALTER TABLE categorias RENAME TO categorias_TODO')

elif opcao == 3:
    cursor.execute('CREATE TABLE tarefas(id_tarefas INT NOT NULL, nome_tarefa VARCHAR(100), status_tarefa VARCHAR(100), id_categorias INT NOT NULL, PRIMARY KEY(id_tarefas),FOREIGN KEY(id_categorias) REFERENCES categorias(id_tarefas));')
conexao.commit()
conexao.close()