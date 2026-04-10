from main import estacionamento

def menu():
    print("Menu de Vagas")
    print("1. Listar Vagas")
    print("2. Alterar status de uma vaga")
    print("3. Sair")
    
def alterar_status(vagas):
    id_vaga = int(input("Digite o ID da vaga que deseja alterar: "))

    estacionamento[id_vaga].alterar_status(not estacionamento[id_vaga].status)

    print("Vaga não encontrada.")
    
def sair():
    print("Saindo do sistema...")
    exit()