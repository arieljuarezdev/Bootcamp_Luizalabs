
# usuarios = []
# contas = []
usuarios = [{'nome': 'aaa', 'cpf': '111', 'dt_nasc': '123123123', 'logr': 'asdasd, dsdsdsdsd - asdasdasdasdasd - dddddd / dd'}]
contas = [
    {'n_agendcia': '0001', 'n_conta': 1, 'usuario': '111', 'saldo': 0, 'limite': 500, 'extrato': '', 'numero_saques': 0, 'LIMITE_SAQUES': 3},
    {'n_agendcia': '0001', 'n_conta': 2, 'usuario': '111', 'saldo': 0, 'limite': 500, 'extrato': '', 'numero_saques': 0, 'LIMITE_SAQUES': 3},
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
    cnt_op ={}
    for conta in contas:
        if conta['usuario'] == cpf:
            cnt_logada.append(conta) 
            cnt_op = conta

    for i, conta in enumerate(cnt_logada):
        print(f"[{i}]: nº da conta:{conta['n_conta']} | CPF: {conta['usuario']}")

    area_operacao(cnt_op)
    

def area_operacao(cnt_acessada):
    acs_conta = int(input("Selecione a conta que desenja acessar. (Ex.: 3) : "))
    cnt_acessada = contas[acs_conta]
    
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
            print(f"\n conta: {cnt_acessada}")

def depositar(dados, valor_dep,/):
    
    
    dados['saldo'] += valor_dep
    print(f"dados em depositar: {dados}")


 
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
