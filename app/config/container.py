from flask import Flask
from app.adapters.input.api.cliente_routes import criar_cliente_blueprint
from app.adapters.output.repositories.cliente_repository_sqlserver import ClienteRepositorySqlServer
from app.application.services.cliente_service import ClienteService


def create_app() -> Flask:
    app = Flask(__name__)

    repository = ClienteRepositorySqlServer()
    service = ClienteService(repository)

    cliente_blueprint = criar_cliente_blueprint(service)
    app.register_blueprint(cliente_blueprint)

    return app