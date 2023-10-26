class ContaBancaria:

    def __init__(self, numero, saldo, nome, tipo, limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = limite

    def depositar(self, deposito):
        if self.status == True:
            self.saldo += deposito
            print(f"Seu saldo foi atualizado para {self.saldo}")
        else:
            print(f"Sua conta ainda nao esta ativa")

    def sacar(self, valorDeSaque):
        if self.status == True:
            if self.saldo > valorDeSaque:
                print(f"Sr(a) {self.nome} seu saque de R$ {valorDeSaque} foi efetuado com sucesso")
                self.saldo -= valorDeSaque
            else:
                print(f"Sr(a) {self.nome} voce nao pode sacar esse valor pois nao tem dinheiro surficiente em sua conta")

        else:
            print(f"Sua conta ainda nao esta ativa")

    def ativarConta(self):
        if self.status ==  False:
            print(f"sua conta foi ativa")
            self.status = True
        else:
            print("sua conta ja esta ativa")


    def verificarSaldo(self):
        if self.status == True:
            print(f"{self.nome} o seu saldo e de R$ {self.saldo}")
        else:
            print(f"Sua conta ainda nao esta ativa")


