# FASTAPI-Evento

# Gerenciamento de Eventos com FastAPI
Esta é uma API simples para gerenciamento de eventos, construída com FastAPI em Python.

Funcionalidades

- Listar todos os produtos
- Obter detalhes de um produto específico por ID
- Criar um novo produto
- Atualizar os detalhes de um produto existente
- Deletar um produto existente

Endpoints

GET /eventos/
Retorna uma lista de todos os eventos.

GET /eventos/{evento_id}
Retorna detalhes de um evento específico com o ID fornecido.

POST /eventos/
Cria um novo evento. Os campos necessários são:

id: ID único do evento (inteiro)
nome: Nome do evento (string)
descricao: Descrição do evento (string)
data: Data do evento (string)
localizacao: Localização do evento (string)

PUT /eventos/{evento_id}
Atualiza os detalhes de um evento existente com o ID fornecido. Os campos necessários são os mesmos que na criação do evento.

DELETE /eventos/{evento_id}
Exclui um evento existente com o ID fornecido.

*Após ter dado GIT CLONE no projeto:*

# Certifique-se de ter todas as dependências instaladas. Você pode instalá-las executando:
- pip install fastapi uvicorn

# Para iniciar o servidor, execute o seguinte comando:
- uvicorn main:app --reload
- O servidor será iniciado em http://127.0.0.1:8000.

# Você pode acessar a documentação interativa da API em:
- http://127.0.0.1:8000/docs
