from main import estacionamento


def contarVagasDisponiveis(estacionamento):
    """Conta quantas vagas estao com status Livre."""
    vagasLivres = 0
    for vaga in estacionamento:
        if vaga.status == "Livre":
            vagasLivres += 1

    return vagasLivres


if __name__ == "__main__":
    print("--- Teste do Contador ---")
    print(f"Total de Vagas: {len(estacionamento)}")
    print(f"Vagas Livres: {contarVagasDisponiveis(estacionamento)}")