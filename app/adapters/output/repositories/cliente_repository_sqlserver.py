from app.domain.entities.cliente import Cliente
from app.domain.ports.cliente_repository import ClienteRepositoryPort
from app.config.database import get_connection


class ClienteRepositorySqlServer(ClienteRepositoryPort):
    def salvar(self, cliente: Cliente) -> None:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO CLIENTES (ID, NOME, EMAIL)
                VALUES (?, ?, ?)
                """,
                (cliente.id, cliente.nome, cliente.email)
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def buscar_por_id(self, cliente_id: int) -> Cliente | None:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                SELECT ID, NOME, EMAIL
                FROM CLIENTES
                WHERE ID = ?
                """,
                (cliente_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Cliente(
                id=row.ID,
                nome=row.NOME,
                email=row.EMAIL
            )
        finally:
            cursor.close()
            conn.close()

    def listar_todos(self) -> list[Cliente]:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                SELECT ID, NOME, EMAIL
                FROM CLIENTES
                ORDER BY ID
                """
            )

            rows = cursor.fetchall()

            return [
                Cliente(
                    id=row.ID,
                    nome=row.NOME,
                    email=row.EMAIL
                )
                for row in rows
            ]
        finally:
            cursor.close()
            conn.close()

    def atualizar(self, cliente: Cliente) -> None:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                UPDATE CLIENTES
                SET NOME = ?, EMAIL = ?
                WHERE ID = ?
                """,
                (cliente.nome, cliente.email, cliente.id)
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def deletar(self, cliente_id: int) -> None:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                DELETE FROM CLIENTES
                WHERE ID = ?
                """,
                (cliente_id,)
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()