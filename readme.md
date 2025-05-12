# Projeto API python 

Projeto feito com a lib fastAPI para consultar dados de questões armazenados no banco de dados in memory redis.

## Setup

1. **Criar container redis**:
    ```sh
        docker run -d --name meu-redis -p 6379:6379 redis
    ```

2. **Install dependencies**:
    ```sh
    pip install fastapi uvicorn redis
    ```

3. **Run the application**:
    ```sh
    uvicorn main:app --reload --log-level info
    ```

## Endpoints

- **GET /**: Returns a welcome message.

## Example

To test the application, run the following command and navigate to `http://127.0.0.1:8000` in your browser:

to see doc swagger:  `http://127.0.0.1:8000/docs`

    ```sh
    uvicorn main:app --reload

    ```

## Para executar

**Pode utilizar a propria pagina do swagger e clicar em try it out e colocar os dados de parametros e body na pagina mesmo!**


## Postman collection

Postman collection on root folder ./redis.postman_collection.json


## Como destruir o container Redis

Para remover o container Redis criado, execute o comando abaixo no terminal:

    ```sh
    docker rm -f meu-redis
    ```
