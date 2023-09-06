```sh
docker compose up
```

Depois de executar o compose:
- O nginx fica disponível na porta 5001. [http://localhost:5001/]
- O app node fica disponível na porta 5002. [http://localhost:5002/]
- O app também fica disponível pelo nginx. [http://localhost:5001/node]
networks:
  q3-net:

volumes:
  q3-vol:

services:
  q3-sql:
    image: postgres:alpine
    networks:
      - q3-net
    volumes:
      - q3-vol:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: confia

  q3-nginx:
    image: nginx:alpine
    ports:
      - "5001:80/tcp"
    networks:
      - q3-net
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - q3-node

  q3-node:
    build: .
    ports:
      - "5002:3000/tcp"
    networks:
      - q3-net
    depends_on:
      - q3-sql
