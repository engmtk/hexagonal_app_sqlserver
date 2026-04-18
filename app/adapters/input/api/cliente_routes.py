from flask import Blueprint, jsonify, request
from app.application.services.cliente_service import ClienteService


def criar_cliente_blueprint(service: ClienteService) -> Blueprint:
    bp = Blueprint("clientes", __name__)

    @bp.route("/clientes", methods=["POST"])
    def criar_cliente():
        try:
            data = request.get_json()

            if not data:
                return jsonify({"erro": "JSON inválido ou não enviado."}), 400

            cliente = service.criar_cliente(
                cliente_id=data["id"],
                nome=data["nome"],
                email=data["email"]
            )

            return jsonify({
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email
            }), 201

        except KeyError as e:
            return jsonify({"erro": f"Campo obrigatório ausente: {str(e)}"}), 400
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400
        except Exception as e:
            return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

    @bp.route("/clientes/<int:cliente_id>", methods=["GET"])
    def buscar_cliente(cliente_id: int):
        try:
            cliente = service.obter_cliente(cliente_id)

            if not cliente:
                return jsonify({"erro": "Cliente não encontrado."}), 404

            return jsonify({
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email
            }), 200
        except Exception as e:
            return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

    @bp.route("/clientes", methods=["GET"])
    def listar_clientes():
        try:
            clientes = service.listar_clientes()

            return jsonify([
                {
                    "id": cliente.id,
                    "nome": cliente.nome,
                    "email": cliente.email
                }
                for cliente in clientes
            ]), 200
        except Exception as e:
            return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

    @bp.route("/clientes/<int:cliente_id>", methods=["PUT"])
    def atualizar_cliente(cliente_id: int):
        try:
            data = request.get_json()

            if not data:
                return jsonify({"erro": "JSON inválido ou não enviado."}), 400

            cliente = service.atualizar_cliente(
                cliente_id=cliente_id,
                nome=data["nome"],
                email=data["email"]
            )

            return jsonify({
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email
            }), 200

        except KeyError as e:
            return jsonify({"erro": f"Campo obrigatório ausente: {str(e)}"}), 400
        except ValueError as e:
            mensagem = str(e)
            if mensagem == "Cliente não encontrado.":
                return jsonify({"erro": mensagem}), 404
            return jsonify({"erro": mensagem}), 400
        except Exception as e:
            return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

    @bp.route("/clientes/<int:cliente_id>", methods=["DELETE"])
    def deletar_cliente(cliente_id: int):
        try:
            service.deletar_cliente(cliente_id)
            return jsonify({"mensagem": "Cliente deletado com sucesso."}), 200

        except ValueError as e:
            mensagem = str(e)
            if mensagem == "Cliente não encontrado.":
                return jsonify({"erro": mensagem}), 404
            return jsonify({"erro": mensagem}), 400
        except Exception as e:
            return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

    return bp