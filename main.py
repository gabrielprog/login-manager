import os

from Database import *
from Banner import *

if __name__ == '__main__':
    database = Database()


    if(os.path.exists("password.txt")):
        password = input("Digite sua senha: ").lower()
        password_storage = open("password.txt", "r")

        if(password_storage.read() == password):
            while (True):

                Banner().banner()
                op = input("Resposta: ")

                if(op == "01" or op == "1"):
                    login = input("Login: ")
                    password = input("Senha: ")
                    description = input("Descrição: ")
                    database.insertLogin(login, password, description)

                elif(op == "02" or op == "2"):
                    database.readLogin()

                elif(op == "03" or op == "3"):
                    op = input("Tem certeza?[Y/N]: ")

                    if(op.upper() == "Y"):
                        database.dropTable()
                        os.unlink("password.txt")
                        exit(0)

                    elif(op.upper() == "N"):
                        pass
                    else:
                        print("Opção invalida")

                elif(op == "00" or op == "0"):
                    break
        else:

            print("Senha incorreta")


    else:

        password_file = open("password.txt", "w")

        Banner().password_banner()

        password = input("Senha: ").lower()

        password_file.write(password)
        password_file.close()

        database.createTable()

