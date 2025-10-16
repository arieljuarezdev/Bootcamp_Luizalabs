# menu = """

# [d] Depositar
# [s] Sacar
# [e] Extrato
# [q] Sair

# => """

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUES = 3

# while True:

#     opcao = input(menu)

#     if opcao == "d":
#         valor = float(input("Informe o valor do depósito: "))

#         if valor > 0:
#             saldo += valor
#             extrato += f"Depósito: R$ {valor:.2f}\n"

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "s":
#         valor = float(input("Informe o valor do saque: "))

#         excedeu_saldo = valor > saldo

#         excedeu_limite = valor > limite

#         excedeu_saques = numero_saques >= LIMITE_SAQUES

#         if excedeu_saldo:
#             print("Operação falhou! Você não tem saldo suficiente.")

#         elif excedeu_limite:
#             print("Operação falhou! O valor do saque excede o limite.")

#         elif excedeu_saques:
#             print("Operação falhou! Número máximo de saques excedido.")

#         elif valor > 0:
#             saldo -= valor
#             extrato += f"Saque: R$ {valor:.2f}\n"
#             numero_saques += 1

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "e":
#         print("\n================ EXTRATO ================")
#         print("Não foram realizadas movimentações." if not extrato else extrato)
#         print(f"\nSaldo: R$ {saldo:.2f}")
#         print("==========================================")

#     elif opcao == "q":
#         break

#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada.")


# usuarios = []
# contas = []
usuarios = [{'nome': 'aaa', 'cpf': '111', 'dt_nasc': '123123123', 'logr': 'asdasd, dsdsdsdsd - asdasdasdasdasd - dddddd / dd'}]
contas = [{'n_ agendcia': '0001', 'n_conta': 1, 'usuario': 'aaa'}]

def criar_usuario(dados):
    print("Usuário cadastrado!")
    usuarios.append(dados)
    criar_conta(dados['cpf']) 
  
def criar_conta(cpf):
    index = len(contas)
    if index <= 1:
        index += 1
    
    dados = {
        "n_ agendcia": "0001",
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
    for conta in contas:
        if conta['usuario'] == cpf:
            cnt_logada.append(conta)
           
    print(f"conta logada: {cnt_logada}")
    

  
def acesso():
    print("========* Acesso a conta *========")
    info = input("Informe o CPF:")  
    
    for usuario in usuarios:
        if info == usuario['cpf']:
            print("==========================")
            area_logada()
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

    print(usuarios)
    print(contas)
    
main()
