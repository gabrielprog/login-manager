class SaveLogin:

    def __init__(self, login, password, description):
        self.login = login
        self.password = password
        self.description = description

    def saveLogin(self):

        print(self.login)
        print(self.password)
        print(self.description)

if __name__ == '__main__':

    obj = SaveLogin("gabriel@gmail.com", "test", "user facebook")
    obj.saveLogin()
