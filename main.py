from classes import ContaCorrente, ContaPoupanca, Cliente, Banco

banco = Banco("NUBANK")

def menu():
    print("""
=======================================
            NUBANK
=======================================
[1] Cadastrar cliente
[2] Abrir conta corrente
[3] Abrir conta poupança
[4] Depositar
[5] Sacar
[6] Transferir
[7] Ver extrato
[8] Listar clientes
[0] Sair
=======================================
    """)
    return input("Escolha uma opção: ")

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    cliente = Cliente(nome, cpf)
    banco.cadastrar_cliente(cliente)

def buscar_conta():
    numero = input("Número da conta: ")
    for conta in banco.contas:
        if str(conta.numero_conta) == numero:
            return conta
    print("Conta não encontrada.")
    return None
    
def abrir_conta_corrente():
    cpf = input("CPF do titular: ")
    cliente = banco.buscar_cliente(cpf)
    if not cliente:
        return
    numero = input("Número da conta: ")
    senha = input("Senha: ")
    limite = float(input("Limite do cheque especial: R$"))
    saldo = float(input("Depósito inicial: R$"))
    conta = ContaCorrente(cliente.nome, numero, senha, limite, saldo)
    banco.abrir_conta(conta, cliente)

def abrir_conta_poupanca():
    cpf = input("CPF do titular: ")
    cliente = banco.buscar_cliente(cpf)
    if not cliente:
        return
    numero = input("Número da conta: ")
    senha = input("Senha: ")
    taxa = float(input("Taxa de juros mensal (ex: 0.05 para 5%): "))
    saldo = float(input("Depósito inicial: R$"))
    conta = ContaPoupanca(cliente.nome, numero, senha, taxa, saldo)
    banco.abrir_conta(conta, cliente)

def depositar():
    conta = buscar_conta()
    if not conta:
        return
    valor = float(input("Valor do depósito: R$"))
    conta.depositar(valor)

def sacar():
    conta = buscar_conta()
    if not conta:
        return
    valor = float(input("Valor do saque: R$"))
    senha = input("Senha: ")
    conta.sacar(valor, senha)

def transferir():
    print("Conta de origem:")
    conta_origem = buscar_conta()
    if not conta_origem:
        return
    print("Conta de destino:")
    conta_destino = buscar_conta()
    if not conta_destino:
        return
    valor = float(input("Valor da transferência: R$"))
    senha = input("Senha da conta de origem: ")
    banco.transferir(conta_origem, conta_destino, valor, senha)

def ver_extrato():
    conta = buscar_conta()
    if not conta:
        return
    conta.extrato()

def listar_clientes():
    banco.listar_clientes()

while True:
    opcao = menu()

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        abrir_conta_corrente()
    elif opcao == "3":
        abrir_conta_poupanca()
    elif opcao == "4":
        depositar()
    elif opcao == "5":
        sacar()
    elif opcao == "6":
        transferir()
    elif opcao == "7":
        ver_extrato()
    elif opcao == "8":
        listar_clientes()
    elif opcao == "0":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")