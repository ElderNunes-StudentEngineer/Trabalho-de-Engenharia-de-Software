from dataclasses import dataclass

@dataclass
class Vaga:
    id: int
    tipo: str
    status: str

    def alterar_status(self, novo_status: str):
            self.status = novo_status
            print(f"Vaga {self.id}: Status atualizado para {self.status}")

    def alterar_tipo(self, novo_tipo: str):
        self.tipo = novo_tipo
        print(f"Vaga {self.id}: Tipo atualizado para {self.tipo}")