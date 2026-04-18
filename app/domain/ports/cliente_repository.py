from abc import ABC, abstractmethod
from app.domain.entities.cliente import Cliente


class ClienteRepositoryPort(ABC):
    @abstractmethod
    def salvar(self, cliente: Cliente) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, cliente_id: int) -> Cliente | None:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Cliente]:
        pass

    @abstractmethod
    def atualizar(self, cliente: Cliente) -> None:
        pass

    @abstractmethod
    def deletar(self, cliente_id: int) -> None:
        pass