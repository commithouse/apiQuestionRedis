# Projeto API python 

Projeto feito com a lib fastAPI para consultar dados de questões armazenados no banco de dados in memory redis.

## Setup

1. **Install dependencies**:
    ```sh
    pip install fastapi uvicorn redis
    ```

2. **Run the application**:
    ```sh
    uvicorn main:app --reload --log-level info
    ```
3. **Clonar projeto**
   ```sh
   git clone https://github.com/commithouse/apiQuestionRedis
   cd apiQuestionRedis
   ```
## Endpoints

- **GET /**: Returns a welcome message.

## Example

To test the application, run the following command and navigate to `http://127.0.0.1:8000` in your browser:

to see doc swagger:  `http://127.0.0.1:8000/docs`

```sh
uvicorn main:app --reload

```

## Postman collection

Postman collection on root folder ./redis.postman_collection.json
