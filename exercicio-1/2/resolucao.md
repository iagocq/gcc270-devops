```sh
docker build -t img-q2 .
docker container run -d -p 5000:3000 --name q2 img-q2
```

Abra o navegador no endereço <http://localhost:5000>
