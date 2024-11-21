FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY ./app.js /app/app.js

EXPOSE 3000

CMD ["node", "server.js"]
