```sh
docker container run --name q1 -itd ubuntu
docker container attach q1
# -- dentro do container -- #
apt update
apt install -y curl
curl --version
```
