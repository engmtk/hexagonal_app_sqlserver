from app.domain.entities.cliente import Cliente
from app.domain.ports.cliente_repository import ClienteRepositoryPort


class ClienteService:
    def __init__(self, repository: ClienteRepositoryPort):
        self.repository = repository

    def criar_cliente(self, cliente_id: int, nome: str, email: str) -> Cliente:
        if not nome or not nome.strip():
            raise ValueError("O nome do cliente é obrigatório.")

        if not email or "@" not in email:
            raise ValueError("E-mail inválido.")

        cliente_existente = self.repository.buscar_por_id(cliente_id)
        if cliente_existente:
            raise ValueError("Já existe cliente com esse ID.")

        cliente = Cliente(
            id=cliente_id,
            nome=nome.strip(),
            email=email.strip()
        )

        self.repository.salvar(cliente)
        return cliente

    def obter_cliente(self, cliente_id: int) -> Cliente | None:
        return self.repository.buscar_por_id(cliente_id)

    def listar_clientes(self) -> list[Cliente]:
        return self.repository.listar_todos()

    def atualizar_cliente(self, cliente_id: int, nome: str, email: str) -> Cliente:
        if not nome or not nome.strip():
            raise ValueError("O nome do cliente é obrigatório.")

        if not email or "@" not in email:
            raise ValueError("E-mail inválido.")

        cliente_existente = self.repository.buscar_por_id(cliente_id)
        if not cliente_existente:
            raise ValueError("Cliente não encontrado.")

        cliente_atualizado = Cliente(
            id=cliente_id,
            nome=nome.strip(),
            email=email.strip()
        )

        self.repository.atualizar(cliente_atualizado)
        return cliente_atualizado

    def deletar_cliente(self, cliente_id: int) -> None:
        cliente_existente = self.repository.buscar_por_id(cliente_id)
        if not cliente_existente:
            raise ValueError("Cliente não encontrado.")

        self.repository.deletar(cliente_id)