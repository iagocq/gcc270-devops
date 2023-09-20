```sh
docker compose up
```

## Criar um item no todo list

curl -X POST -F "texto=um texto" http://localhost:5000/criar

## Listar os itens

curl http://localhost:5000

## Marcar item como feito

curl http://localhost:5000/pronto/1
