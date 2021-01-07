# -*- coding: utf-8 -*-

#Modulos

from PyQt5 import uic,QtWidgets
import sqlite3

##Parte do login

def chamar_logout() :
    Login.label_4.setText("")
    nome_usuario = Login.lineEdit_2.text()
    password_usuario = Login.lineEdit.text()
    banco = sqlite3.connect('cadastro.db')
    cursor = banco.cursor()

    try:
        cursor.execute("SELECT senha FROM dados_de_cadastro WHERE login = '{}'".format(nome_usuario))
        senha_bd = cursor.fetchall()
        print(senha_bd [0] [0] )
        banco.close()

    except:
        print("Erro ao validar o login!")

    if password_usuario == senha_bd [0] [0] :
        Login.close()
        logout.show()
    else:
        Login.label_5.setText("Os dados de usuario e senha nao estao corretos!")


#Parte de Logout

def chamar_login() : 

    logout.close()
    Login.show()

#Abrir o cadastro

def abre_tela_cadastro() :
    cadastro.show()

#Cadastrar

def cadastrar() :
    
    nome = cadastro.lineEdit.text()
    login = cadastro.lineEdit_4.text()
    senha = cadastro.lineEdit_2.text()
    c_senha = cadastro.lineEdit_3.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS dados_de_cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO dados_de_cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")
            
            banco.commit()
            banco.close()
            cadastro.label_5.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados:",erro)
    else:
        cadastro.label_5.setText('As senhas estao diferentes')


#Configuraçao do Qt e conecçao de arquivos

app=QtWidgets.QApplication([])
Login = uic.loadUi("Login.ui")
logout = uic.loadUi("Logout.ui")
cadastro = uic.loadUi("Cadastro.ui")
Login.pushButton.clicked.connect(chamar_logout)
logout.pushButton.clicked.connect(chamar_login)
Login.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
Login.pushButton_2.clicked.connect(abre_tela_cadastro)
cadastro.pushButton.clicked.connect(cadastrar)

Login.show()
app.exec()
