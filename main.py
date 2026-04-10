from vaga import Vaga 

estacionamento = [Vaga(id=i, tipo="Reservada" if i <= 20 else "Comum", status="Livre") for i in range(1, 101)]