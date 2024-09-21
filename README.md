
## Como Baixar o Projeto

Para baixar este projeto do GitHub, siga os passos abaixo:

1. **Clone o repositório**:
   Abra seu terminal e execute o seguinte comando:
   ```bash
   git clone https://github.com/usuario/nome-do-repositorio.git
   ```
   
2. **Navegue até a pasta do projeto**:
   ```bash
   cd nome-do-repositorio
   ```

3. **Siga as instruções de instalação**:
   Continue com as instruções de instalação do ambiente virtual e bibliotecas necessárias.

## Como Rodar com VENV (Ambiente Virtual Python)

Este projeto foi inicialmente desenvolvido para rodar utilizando um ambiente virtual Python. Abaixo, forneceremos um guia completo de instalação para rodar sua API em qualquer sistema operacional:

## Windows(CMD/Powershell):

1. Criando o VENV

   Primeiro, você deve abrir este projeto no seu terminal e executar os seguintes comandos na pasta raiz do seu projeto.
   Abaixo está o comando para criar um ambiente virtual Python (venv):

   ```commandline
   python -m venv venv
   ```

2. Ativando o Ambiente Virtual

   Execute o comando abaixo para ativar o seu venv na sessão atual do terminal:

   ```commandline
   .\venv\Scripts\activate
   ```

   O comando acima funciona bem para CMD ou Powershell. Se você estiver utilizando o Git Bash para rodar esses comandos, execute o seguinte comando:

   ```bash
   source venv/Scripts/activate
   ```

3. Instalar as Bibliotecas Necessárias para sua API

   Este projeto requer várias bibliotecas armazenadas no PyPi para rodar. Todas elas estão listadas no arquivo requirements.txt na pasta raiz do projeto gerado. Para instalá-las, execute o comando abaixo::

   ```commandline
    pip install -r requirements.txt
   ```

4. Rodar o app.py

   Após a instalação das bibliotecas ser concluída, você pode utilizar o comando abaixo para rodar o projeto:

   ```bash
   python app.py
   ```

## API Endpoints

## Como Acessar a Documentação da API com Swagger

1. **Acesse o Swagger**:
Abra o seu navegador e digite a seguinte URL:
**[http://localhost:5000/swagger/](http://localhost:5000/apidocs/#/default/get_companies)**

2. **Interaja com a API**:
Uma vez na página do Swagger, você verá uma lista das rotas disponíveis. Clique na rota desejada para expandir suas opções. Você pode visualizar a documentação e testar as requisições diretamente pela interface.

3. **Realize Requisições**:
Para testar uma requisição:
- Clique no botão **"Try it out"**.
- Preencha os parâmetros necessários no corpo da requisição.
- Clique em **"Execute"** para enviar a requisição e visualizar a resposta diretamente no Swagger.


### Criar Empresa

**Endpoint:** `/company`  
**Método:** `POST`  
**Descrição:** Cria uma nova empresa no banco de dados.

**Requisição:**

- **URL:** `/company`
- **Método:** `POST`
- **Cabeçalhos:**
  - `Content-Type: application/json`
- **Corpo da Requisição:**
  ```json
  {
    "cnpj": "12345678000195", //user o gerador de CNPJ: https://www.4devs.com.br/gerador_de_cnpj
    "register_name": "Nome Registrado da Empresa",
    "business_name": "Nome Fantasia da Empresa",
    "cnae": "1234567"
  }
  ```

**Respostas:**

- **Sucesso:**

  - **Código:** `201 Created`
  - **Corpo:**
    ```json
    {
      "data": {
        "id": 1,
        "cnpj": "12345678000195",
        "register_name": "Nome Registrado da Empresa",
        "business_name": "Nome Fantasia da Empresa",
        "cnae": "1234567"
      },
      "message": "Empresa registrada com sucesso"
    }
    ```

- **Erro:**
  - **Código:** `400 Bad Request`
  - **Corpo (CNPJ já existente):**
    ```json
    {
      "message": "Já existe empresa com este CNPJ."
    }
    ```
  - **Corpo (Nome registrado já existente):**
    ```json
    {
      "message": "Já existe empresa com este nome registrado."
    }
    ```
  - **Corpo (Dados inválidos):**
    ```json
    {
      "message": "Campo obrigatório ausente ou vazio: {campo}"
    }
    ```
  - **Corpo (CNPJ inválido):**
    ```json
    {
      "message": "CNPJ inválido. O número não corresponde a um CNPJ válido."
    }
    ```

## Listar Empresas

**Endpoint:** `/companies`  
**Método:** `GET`  
**Descrição:** Retorna uma lista de empresas com opções de paginação e ordenação.

**Requisição:**

- **URL:** `/companies`
- **Método:** `GET`
- **Parâmetros da Query:**
  - `offset` (opcional): Número de registros a serem pulados (padrão: 0).
  - `limit` (opcional): Número de registros a serem retornados por página (padrão: 20).
  - `sort` (opcional): Campo pelo qual ordenar os resultados (padrão: `created_at`). Os campos válidos são: `id`, `cnpj`, `register_name`, `business_name`, `cnae`, `created_at`.
  - `dir` (opcional): Direção da ordenação (`asc` ou `desc`, padrão: `asc`).

**Exemplo de Requisição:**
**Respostas:**

- **Sucesso:**

  - **Código:** `200 OK`
  - **Corpo:**
    ```json
    {
      "data": {
        "total_companies": 100,
        "total_pages": 5,
        "current_page": 1,
        "empresas": [
          {
            "cnpj": "12345678000195",
            "register_name": "Nome Registrado da Empresa",
            "business_name": "Nome Fantasia da Empresa",
            "cnae": "1234567",
            "created_at": "2024-01-01T00:00:00Z",
            "deleted_at": null
          },
          ...
        ]
      },
      "message": "Lista de empresas retornada com sucesso"
    }
    ```

- **Erro:**
  - **Código:** `400 Bad Request`
  - **Corpo (Campo de ordenação inválido):**
    ```json
    {
      "message": "Campo de ordenação inválido"
    }
    ```
  - **Corpo (Parâmetro 'dir' inválido):**
    ```json
    {
      "message": "Parâmetro 'dir' inválido. Use 'asc' ou 'desc'."
    }
    ```
  - **Corpo (Página inválida):**
    ```json
    {
      "message": "Página inválida. Não há mais registros."
    }
    ```

## Obter Empresa com detalhes

**Endpoint:** `/company`  
**Método:** `GET`  
**Descrição:** Retorna os detalhes de uma empresa com base no CNPJ fornecido.

**Requisição:**

- **URL:** `/company`
- **Método:** `GET`
- **Parâmetros da Query:**
  - `cnpj` (obrigatório): O CNPJ da empresa a ser buscada.

**Exemplo de Requisição:**
http
GET /company?cnpj=12345678000195
**Respostas:**

- **Sucesso:**

  - **Código:** `200 OK`
  - **Corpo:**
    ```json
    {
      "data": {
        "cnpj": "12345678000195",
        "register_name": "Nome Registrado da Empresa",
        "business_name": "Nome Fantasia da Empresa",
        "cnae": "1234567",
        "created_at": "2024-01-01T00:00:00Z",
        "deleted_at": null
      },
      "message": "Empresa encontrada com sucesso"
    }
    ```

- **Erro:**
  - **Código:** `400 Bad Request`
  - **Corpo (CNPJ não fornecido):**
    ```json
    {
      "message": "CNPJ não fornecido."
    }
    ```
  - **Código:** `404 Not Found`
  - **Corpo (Empresa não encontrada):**
    ```json
    {
      "message": "Empresa não encontrada"
    }
    ```
  - **Código:** `500 Internal Server Error`
  - **Corpo (Erro ao buscar a empresa):**
    ```json
    {
      "message": "Erro ao buscar a empresa: [mensagem de erro]"
    }
    ```

## Atualizar Empresa

**Endpoint:** `/company/<id>`  
**Método:** `PUT`  
**Descrição:** Atualiza os detalhes de uma empresa com base no ID fornecido.

**Requisição:**

- **URL:** `/company/<id>`
- **Método:** `PUT`
- **Parâmetros:**
  - `id` (obrigatório): O ID da empresa a ser atualizada.
- **Corpo da Requisição (JSON):**
  - `business_name` (opcional): Novo nome fantasia da empresa.
  - `cnae` (opcional): Novo código CNAE da empresa.

**Exemplo de Requisição:**
http
PUT /company/1
Content-Type: application/json
{
"business_name": "Novo Nome Fantasia",
"cnae": "7654321"
}
**Respostas:**

- **Sucesso:**

  - **Código:** `200 OK`
  - **Corpo:**
    ```json
    {
      "data": {
        "cnpj": "12345678000195",
        "register_name": "Nome Registrado da Empresa",
        "business_name": "Novo Nome Fantasia",
        "cnae": "7654321",
        "created_at": "2024-01-01T00:00:00Z",
        "deleted_at": null
      },
      "message": "Empresa atualizada com sucesso"
    }
    ```

- **Erro:**

  - **Código:** `404 Not Found`
  - **Corpo (Empresa não encontrada):**
    ```json
    {
      "message": "Company not found"
    }
    ```
  - **Código:** `400 Bad Request`
  - **Corpo (Dados de atualização inválidos):**
    ```json
    {
      "message": "[mensagem de erro específica]"
    }
    ```
  - **Código:** `500 Internal Server Error`
  - **Corpo (Erro ao atualizar a empresa):**
    `json
{
  "message": "Error ao Atualizar empresa: [mensagem de erro]"
}
`

## Deletar Empresa

**Endpoint:** `/company/<id>`  
**Método:** `DELETE`  
**Descrição:** Exclui uma empresa do banco de dados com base no ID fornecido.

**Requisição:**

- **URL:** `/company/<id>`
- **Método:** `DELETE`
- **Parâmetros:**
  - `id` (obrigatório): O ID da empresa a ser excluída.

**Exemplo de Requisição:**
http
DELETE /company/1

**Respostas:**

- **Sucesso:**

  - **Código:** `204 No Content`
  - **Corpo:** (vazio)

- **Erro:**
  - **Código:** `404 Not Found`
  - **Corpo (Empresa não encontrada):**
    ```json
    {
      "message": "Company not found"
    }
    ```
  - **Código:** `400 Bad Request`
  - **Corpo (Empresa já está excluída):**
    ```json
    {
      "message": "Empresa já está excluída"
    }
    ```
  - **Código:** `500 Internal Server Error`
  - **Corpo (Erro ao excluir a empresa):**
    ```json
    {
      "message": "Error ao excluir empresa: [mensagem de erro]"
    }
    ```
