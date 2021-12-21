class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

class Wallet:
    def __init__(self, client, balance):
        self.client = client
        self.balance = balance

    def get_client(self):
        return self.client

    def get_balance(self):
        return self.balance