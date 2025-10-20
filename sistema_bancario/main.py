
# usuarios = []
# contas = []
usuarios = [{'nome': 'aaa', 'cpf': '111', 'dt_nasc': '123123123', 'logr': 'asdasd, dsdsdsdsd - asdasdasdasdasd - dddddd / dd'}]
contas = [
    {'n_agendcia': '0001', 'n_conta': 1, 'usuario': '111', 'saldo': 0, 'limite': 500, 'extrato': '', 'numero_saques': 0, 'LIMITE_SAQUES': 3},
    {'n_agendcia': '0001', 'n_conta': 2, 'usuario': '111', 'saldo': 100.0, 'limite': 500, 'extrato': '', 'numero_saques': 0, 'LIMITE_SAQUES': 3},
    ]

def criar_usuario(dados):
    print("Usuário cadastrado!")
    usuarios.append(dados)
    criar_conta(dados['cpf']) 
  
def criar_conta(cpf):
    index = len(contas)
    if index <= 1:
        index += 1
    
    dados = {
        "n_agendcia": "0001",
        "n_conta":index,
        "usuario": cpf,
        "saldo": 0,
        "limite": 500,
        "extrato": "",
        "numero_saques": 0,
        "LIMITE_SAQUES": 3,
    }
    contas.append(dados)
 
def area_logada(cpf):
    cnt_logada = []
    # cnt_op ={}
    for conta in contas:
        if conta['usuario'] == cpf:
            cnt_logada.append(conta) 
            # cnt_op = conta

    for i, conta in enumerate(cnt_logada):
        print(f"[{i}]: nº da conta:{conta['n_conta']} | CPF: {conta['usuario']}")

    acs_conta = int(input("Selecione a conta que desenja acessar. (Ex.: 3) : "))
    cnt_acessada = contas[acs_conta]
    area_operacao(cnt_acessada)
    

def area_operacao(cnt_acessada):
    
    print("========* Conta acessada *==========")
    print(f"nº da conta:{cnt_acessada["n_conta"]} | CPF: {cnt_acessada["usuario"]}")
    
    act = input("""[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Selecione a ação desejada:""")
    
    # print(f"conta logada: {cnt_logada}")
    match act:
        case "d":
            print("========* Deposito *==========")
            valor = float(input("Informe o valor: R$ "))
            dep = depositar(cnt_acessada, valor)
            print(f"\n Novo saldo: {dep}")
            # print(f"\n conta: {cnt_acessada}")
            area_operacao(cnt_acessada)

        case "s":
            print("========* Saque *==========")
            valor = float(input("Informe o valor: R$ "))
            saque, saldo = sacar(val=valor, conta=cnt_acessada)
            print(f'valor sacado: R${saque} | Saldo atual: R$ {saldo}')
            area_operacao(cnt_acessada)
            
        case "e":
            print("========* Extrato *==========")
            ext = extrato(cnt_acessada['extrato'], conta= cnt_acessada )
            print(ext)
            area_operacao(cnt_acessada)

            
def depositar(dados, valor_dep):
    
    
    dados['saldo'] += valor_dep
    print(f"dados em depositar: {dados}")
    return dados['saldo']

def sacar(val, conta):
    excedeu_saldo = val > conta['saldo']
    excedeu_limite = val >conta['limite']
    excedeu_saques = conta['numero_saques'] >= conta['LIMITE_SAQUES']

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif val > 0:
        conta['saldo'] -= val
        # extrato += f"Saque: R$ {valor:.2f}\n"
        conta['numero_saques'] += 1
        return val, conta['saldo']

    else:
        print("Operação falhou! O valor informado é inválido.")
 
def extrato(ext, /, **conta):
    # print(ext, conta)
    # dados = 
    ext = f"nº da conta: {conta['conta']['n_conta']}|saldo atual: R$ {conta['conta']['saldo']} | "
    return ext

def acesso():
    print("========* Acesso a conta *========")
    info = input("Informe o CPF:")  
    
    for usuario in usuarios:
        if info == usuario['cpf']:
            print("==========================")
            area_logada(info)
        else:
            
            print("\n==========================")
            print("Cpf informado, não encontrado, tente novamente!")
            acesso()   
    
def menu():
    info = input("""
=======================================
         Informe a operação:
        [a] Acessar conta.
        [c] Criar conta.
=======================================
Digite a opção e aperte enter: """)

    match info:
        case "a":
            if usuarios != []:
                acesso()
            else:
                cad = input("""
=======================================
Não existem contas cadastradas.
Deseja criar uma conta? [s/n]: """)

        
                if cad != "s" and cad != "n":
                    print("=======================================")
                    print("Resposta inesperada, tente novamente!.")
                    menu()
                else:
                    if cad == "n":
                        print("=======================================")
                        print("Muito obrigada(o) e até a próxima.")
                    else:
                        guarda_dados()
                        
        case "c":
            guarda_dados()

        case _:
            print("=======================================")
            print("Resposta inesperada, tente novamente!.")
            menu()

def guarda_dados():
    print ("============* Criar Conta *===============")
    print ("Informe seus dados:")
    nome = input("Nome completo:")
    cpf = input ("CPF (apenas números): ")
    dt_nasc = input("Dt. Nasc. (dd/mm/aaaa): ")
    print ("======* Endereço *========")
    logr = input("Logradouro: ")
    num = input("Nº: ")
    bairro = input("Bairro: ")
    cid = input("Cidade: ")
    uf = input("UF: ")
    print ("=======================================")
    conf = input("Confirme, os dados estão corretos? [s/n]: ")
    if conf != "s" and conf != "n":
        print("=======================================")
        print("Resposta inesperada, tente novamente.")
        guarda_dados()
    else:
        if conf != "n":
            dados ={
                "nome":nome,
                "cpf":cpf,
                "dt_nasc": dt_nasc,
                "logr": f'{logr}, {num} - {bairro} - {cid} / {uf}'  
            }
            criar_usuario(dados) 
        
        else:
            print("Ok, insira novamente os dados.")
            guarda_dados()  

def main():
    menu()

    # print(usuarios)
    # print(contas)
    
main()
