from app.config.database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO CLIENTES (ID, NOME, EMAIL) VALUES (?, ?, ?)",
    (99, "Teste Direto", "teste@direto.com")
)
conn.commit()

print("Insert realizado com sucesso.")

cursor.close()
conn.close()