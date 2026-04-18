Projeto: Arquitetura Hexagonal com Python e SQL Server

1. Visão Geral
Este projeto demonstra uma aplicação backend utilizando Arquitetura Hexagonal (Ports and Adapters) com Python, Flask e SQL Server. O objetivo é separar a lógica de negócio das dependências externas.

2. Conceitos da Arquitetura Hexagonal
- Domain: contém as entidades e regras centrais.
- Ports: contratos/interfaces que definem como o sistema interage.
- Application: casos de uso.
- Adapters: implementações externas (API, banco de dados).
- Config: montagem das dependências.

3. Estrutura do Projeto

app/
 ├── domain/
 │   ├── entities/
 │   └── ports/
 ├── application/
 │   └── services/
 ├── adapters/
 │   ├── input/api/
 │   └── output/repositories/
 ├── config/
main.py
.env

4. Regras de Negócio
- Cliente deve ter nome válido
- Email deve conter "@"
- Não permite ID duplicado
- Não atualiza cliente inexistente
- Não deleta cliente inexistente

5. Rotas da API
POST /clientes
GET /clientes
GET /clientes/<id>
PUT /clientes/<id>
DELETE /clientes/<id>
6. Como Executar
1. Criar ambiente virtual
2. Instalar dependências
3. Configurar .env
4. Executar python main.py
7. Exemplos de Teste

POST:
curl -X POST http://127.0.0.1:5000/clientes -H "Content-Type: application/json" -d "{\"id\":1,\"nome\":\"Alexandre\",\"email\":\"alexandre@email.com\"}"

GET:
curl http://127.0.0.1:5000/clientes

PUT:
curl -X PUT http://127.0.0.1:5000/clientes/1 -H "Content-Type: application/json" -d "{\"nome\":\"Novo Nome\",\"email\":\"novo@email.com\"}"

DELETE:
curl -X DELETE http://127.0.0.1:5000/clientes/1


