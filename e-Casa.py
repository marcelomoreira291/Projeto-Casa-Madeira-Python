import sqlite3
import database
from PyQt5 import uic, QtWidgets

conexao = database.conectar()
database.criar_tabela_usuarios(conexao)
database.criar_tabela_pedidos(conexao)
database.criar_tabela_caixa(conexao)
database.criar_tabela_estoque_materiais(conexao)
database.criar_tabela_estoque_epis(conexao)

def login(): #corrigir erro usuario_digitaimport sqlite3 as sql 
    usuario_digitado = tela_login.lineEdit_login_usuario.text()
    senha_digitada = tela_login.lineEdit_senha_usuario.text()

    banco = sqlite3.connect("banco_ecm.db")
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios_banco = cursor.fetchall()
    for dados in usuarios_banco:
        if usuario_digitado == dados[1]:
            if senha_digitada == dados[2]:
                tela_login.close()
                tela_logon.show()
                tela_logon.saldacao.setText(f"Seja bem vindo ao Casa & Madeira, {dados[0]}")
        else:
            tela_login.label_erro_login.setText("Usuário ou Senha incorreto(a)")

def pedidos():
    tela_pedidos.show()
    banco = sqlite3.connect("banco_ecm.db")
    cursor = banco.cursor()
    cursor.execute("select * from pedidos")
    dados_pedidos = cursor.fetchall()

    tela_pedidos.tableWidget_pedidos.setRowCount(len(dados_pedidos))
    tela_pedidos.tableWidget_pedidos.setColumnCount(5)
    for i in range(0, len(dados_pedidos)):
        for j in range(0, 5):
            tela_pedidos.tableWidget_pedidos.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_pedidos[i][j])))
    banco.close()

def novo_pedido():
    tela_novo_pedido.show()
    try:
        conexao = database.conectar()
        numero_pedido = tela_novo_pedido.lineEdit_1_numero_pedido.text()
        cliente = tela_novo_pedido.lineEdit_2_cliente.text()
        descricao_pedido = tela_novo_pedido.lineEdit_6_descricao_pedido.text()
        data_pedido = tela_novo_pedido.lineEdit_4_data_pedido.text()
        valor_pedido = tela_novo_pedido.lineEdit_3_valor_pedido.text()
        database.inserir_novo_pedido(conexao, numero_pedido, cliente, descricao_pedido, data_pedido, valor_pedido)
        tela_novo_pedido.label_6_mensagem.setText("Dados inseridos com sucesso!")
    except sqlite3.Error as erro:
        tela_novo_pedido.label_6_mensagem.setText(f"Ocorreu um erro {erro}, verifique os dados inserido.")
    
    

def caixa():
    tela_caixa.show()

def estoque_materiais():
    tela_estoque_materiais.show()

def estoque_epis():
    tela_estoque_epis.show()

def sair():
    exit()

app = QtWidgets.QApplication([])
tela_login = uic.loadUi("tela_login.ui")
tela_erro_login = uic.loadUi("tela_erro_login.ui")
tela_login.pushButton_enviar_dados.clicked.connect(login)
tela_login.pushButton_esqueceu_senha.clicked.connect(tela_erro_login.show)
tela_erro_login.pushButton_voltar_login.clicked.connect(tela_login.show)

tela_logon = uic.loadUi("tela_logon.ui")
tela_logon.pushButton_ver_pedidos.clicked.connect(pedidos)
tela_logon.pushButton_2_ver_caixa.clicked.connect(caixa)
tela_logon.pushButton_3_ver_estoque_materiais.clicked.connect(estoque_materiais)
tela_logon.pushButton_4_ver_estoque_epis.clicked.connect(estoque_epis)

tela_pedidos = uic.loadUi("tela_pedidos.ui")
tela_novo_pedido = uic.loadUi("tela_novo_pedido.ui")
tela_pedidos.pushButton_5_novo_pedido.clicked.connect(tela_novo_pedido.show)
tela_novo_pedido.pushButton_salvar_dados.clicked.connect(novo_pedido)


tela_caixa = uic.loadUi("tela_caixa.ui")


tela_estoque_materiais = uic.loadUi("tela_estoque_materiais.ui")


tela_estoque_epis = uic.loadUi("tela_estoque_epis.ui")


tela_login.show()
app.exec()