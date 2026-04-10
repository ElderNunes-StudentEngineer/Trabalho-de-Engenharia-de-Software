from main import estacionamento


def contarVagasDisponiveis(estacionamento):
    """Conta quantas vagas estao com status Livre."""
    vagasLivres = 0
    for vaga in estacionamento:
        status_livre = vaga.status if isinstance(vaga.status, bool) else str(vaga.status).strip().lower() == "livre"
        if status_livre:
            vagasLivres += 1

    return vagasLivres


if __name__ == "__main__":
    print("--- Teste do Contador ---")
    print(f"Total de Vagas: {len(estacionamento)}")
    print(f"Vagas Livres: {contarVagasDisponiveis(estacionamento)}")