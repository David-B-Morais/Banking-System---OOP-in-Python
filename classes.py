from datetime import datetime

class ContaBancaria:
    """
    Cria uma conta bancária e permite a realização de saques e depósitos.
    """
    def __init__(self, titular, numero_conta, senha, saldo = 0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.__senha = senha
        self._saldo = saldo
        self._historico = []
        print(f"Conta {self.numero_conta} do titular {self.titular} criada com sucesso. Saldo atual de R${self._saldo:.2f}")

    def __str__(self):
        return f"A conta {self.numero_conta} do titular {self.titular} tem R${self._saldo:.2f} de saldo."
    
    def verificar_senha(self, senha):
        return senha == self.__senha

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.append(Transacao("Depósito", valor))
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
    
    def sacar(self, valor, senha):
        if not self.verificar_senha(senha):
            print("Operação negada: SENHA INCORRETA")
            return False
        if valor <= self._saldo:
            self._saldo -= valor
            self._historico.append(Transacao("Saque", valor))
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True
        else:
            print(f"Saque NEGADO de R${valor:.2f}: SALDO INSUFICIENTE")
            return False
        
    def extrato(self):
        print(f"\n===== EXTRATO - Conta {self.numero_conta} =====")
        if not self._historico:
            print("Nenhuma transação registrada.")
        else:
            for transacao in self._historico:
                print(transacao)
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("==========================================\n")

class ContaCorrente(ContaBancaria):
    """
    Conta corrente com limite de cheque especial.
    """
    def __init__(self, titular, numero_conta, senha, limite, saldo = 0):
        super().__init__(titular, numero_conta, senha, saldo)
        self._limite = limite

    def __str__(self):
        return f"[Corrente] Conta {self.numero_conta} do titular {self.titular} tem R${self._saldo:.2f} de saldo e R${self._limite:.2f} de limite."

    def sacar(self, valor, senha):
        if not self.verificar_senha(senha):
            print("Operação negada: senha incorreta.")
            return False
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
            self._historico.append(Transacao("Saque", valor))
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True
        else:
            print(f"Saque NEGADO de R${valor:.2f}: LIMITE INSUFICIENTE")
            return False

class ContaPoupanca(ContaBancaria):
    """
    Conta poupança com rendimento mensal.
    """
    def __init__(self, titular, numero_conta, senha, taxa_juros, saldo = 0):
        super().__init__(titular, numero_conta, senha, saldo)
        self.taxa_juros = taxa_juros

    def __str__(self):
        return f"[Poupança] Conta {self.numero_conta} do titular {self.titular} tem R${self._saldo:.2f} de saldo e de {self.taxa_juros:.1%} ao mês."
    
    def render_juros(self):
        rendimento = self._saldo * self.taxa_juros
        self._saldo += rendimento
        self._historico.append(Transacao("Rendimento de juros", rendimento))
        print(f"Rendimento de R${rendimento:.2f} aplicado. Novo saldo: R${self._saldo:.2f}")

class Transacao:
    """
    Registra uma operação realizada em uma conta bancária, armazenando o tipo, o valor e a data/hora da operação.
    """
    def __init__(self, tipo, valor): # tipo = tipo da operação (ex.: depósito, saque...)
        self.tipo = tipo
        self.valor = valor
        self.data_hora = datetime.now()

    def __str__(self):
        return f"[{self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}] {self.tipo}: R${self.valor:.2f}"

class Cliente:
    """
    Representa um cliente do banco com suas contas vinculadas.
    """
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        if conta in self.contas:
            print(f"A conta {conta.numero_conta} já está vinculada a este cliente.")
        else:
            self.contas.append(conta)
            print(f"A conta {conta.numero_conta} foi vinculada com sucesso ao cliente {self.nome}.")

    def listar_contas(self):
        for conta in self.contas:
            print(conta)

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf} | Contas vinculadas: {len(self.contas)}"
        
class Banco:
    """
    Representa um banco com seus clientes e contas cadastradas.
    """
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, novo_cliente):
        for cliente in self.clientes:
            if cliente.cpf == novo_cliente.cpf:
                print(f"Não foi possível cadastrar: já existe um cliente com o CPF {novo_cliente.cpf}.")
                return
        self.clientes.append(novo_cliente)
        print(f"Cliente {novo_cliente.nome} cadastrado com sucesso.")

    def abrir_conta(self, conta, cliente):
        if cliente not in self.clientes:
            print("Não foi possível abrir a conta: cliente não cadastrado no banco.")
            return
        self.contas.append(conta)
        cliente.adicionar_conta(conta)

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        print("Nenhum cliente com o CPF informado foi encontrado.")
        return None

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def __str__(self):
        return f"Banco: {self.nome} | Clientes cadastrados: {len(self.clientes)} | Contas abertas: {len(self.contas)}"
    
    def transferir(self, conta_origem, conta_destino, valor, senha): # Onde "senha" é a senha da conta de origem
        if conta_origem not in self.contas or conta_destino not in self.contas:
            print("Não foi possível realizar a transferência: conta não encontrada.")
            return
        if conta_origem == conta_destino:
            print("Não foi possível realizar a transferência: conta de origem e destino são iguais.")
            return
        if (conta_origem.sacar(valor, senha)):
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")