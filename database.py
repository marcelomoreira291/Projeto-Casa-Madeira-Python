import sqlite3

#Cria as tabelas
CRIAR_TABELA_USUARIOS = "create table if not exists usuarios (nome text, nome_login text, senha_login text)"
CRIAR_TABELA_PEDIDOS = "create table if not exists pedidos (numero_pedido integer, cliente text, descricao_pedido text, data_pedido real, valor_pedido float);"
CRIAR_TABELA_CAIXA = "create table if not exists caixa (movimento text, valor_caixa float, data_caixa real, descricao_caixa text);"
CRIAR_TABELA_ESTOQUE_MATERIAL = "create table if not exists estoque_materiais( codigo_material integer, descricao_material text, quantidade_material float, valor_material float);"
CRIAR_TABELA_ESTOQUE_EPIS = "create table if not exists estoque_epis (codigo_epis integer, descricao_epis text, quantidade_epis integer, valor_epis float);"

#Insere dados nas tabelas
INSERIR_NOVO_PEDIDO = "insert into pedidos (numero_pedido, cliente, descricao_pedido, data_pedido, valor_pedido) values(?, ?, ?, ?, ?);"
INSERIR_NOVO_MOVIMENTO_CAIXA = "insert into caixa (movimento, valor_caixa, data_caixa, descricao_caixa) values(?, ?, ?, ?);"
INSERIR_NOVO_MATERIAL = "insert into estoque_materiais (codigo_material, descricao_material, quantidade_material, valor_material) values(?, ?, ?, ?);"
INSERIR_NOVO_EPIS = "insert into estoque_epis (codigo_epis, descricao_epis, quantidade_epis, valor_epis) values(?, ?, ?, ?);"

#Exibe dados das tabelas
EXIBE_DADOS_PEDIDOS = "select * from pedidos;"
EXIBE_DADOS_CAIXA = "select * from caixa;"
EXIBE_DADOS_ESTOQUE_MATERIAIS = "select * from estoque_materias;"
EXIBE_DADOS_ESTOQUE_EPIS = "select * from estoque_epis;"

conexao = sqlite3.connect("banco_ecm.db")

def conectar():
    return sqlite3.connect("banco_ecm.db")

def criar_tabela_usuarios(conexao):
    with conexao:
        conexao.execute(CRIAR_TABELA_USUARIOS)

def criar_tabela_pedidos(conexao):
    with conexao:
        conexao.execute(CRIAR_TABELA_PEDIDOS)

def criar_tabela_caixa(conexao):
    with conexao:
        conexao.execute(CRIAR_TABELA_CAIXA)

def criar_tabela_estoque_materiais(conexao):
    with conexao:
        conexao.execute(CRIAR_TABELA_ESTOQUE_MATERIAL)

def criar_tabela_estoque_epis(conexao):
    with conexao:
        conexao.execute(CRIAR_TABELA_ESTOQUE_EPIS)

def inserir_novo_pedido(conexao, numero_pedido, cliente, descricao_pedido, data_pedido, valor_pedido):
    with conexao:
        conexao.execute(INSERIR_NOVO_PEDIDO, (numero_pedido, cliente, descricao_pedido, data_pedido, valor_pedido))

def inserir_novo_movimento_caixa(conexao, movimento, valor_caixa, data_caixa, descricao_caixa):
    with conexao:
        conexao.execute(INSERIR_NOVO_MOVIMENTO_CAIXA, movimento, valor_caixa, data_caixa, descricao_caixa)

def inserir_novo_material(conexao, codigo_material, descricao_material, quantidade_material, valor_material):
    with conexao:
        conexao.execute(codigo_material, descricao_material, quantidade_material, valor_material)

def inserir_novo_epis(conexao, codigo_epis, descricao_epis, quantidade_epis, valor_epis):
    with conexao:
        conexao.execute(codigo_epis, descricao_epis, quantidade_epis, valor_epis)

def exibe_dados_pedidos(conexao):
    with conexao:
        return conexao.execute(EXIBE_DADOS_PEDIDOS).fetchall()

def exibe_dados_pedidos(conexao):
    with conexao:
        return conexao.execute(EXIBE_DADOS_CAIXA).fetchall()

def exibe_dados_pedidos(conexao):
    with conexao:
        return conexao.execute(EXIBE_DADOS_ESTOQUE_MATERIAIS).fetchall()

def exibe_dados_pedidos(conexao):
    with conexao:
        return conexao.execute(EXIBE_DADOS_ESTOQUE_EPIS).fetchall()                        