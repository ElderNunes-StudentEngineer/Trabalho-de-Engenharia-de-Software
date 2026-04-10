def estadoVaga(status):
    if status == "o":
        return "Vaga Ocupada"
    elif status == "l": 
        return "Vaga Livre"

def tipoVaga(tipo):
    if tipo == "c":
        return "Vaga Comum"
    elif tipo == "r":
        return "Vaga Reservada"
    