FROM node:alpine

COPY . /app
WORKDIR /app

RUN npm install express

EXPOSE 3000
ENTRYPOINT node app.js
