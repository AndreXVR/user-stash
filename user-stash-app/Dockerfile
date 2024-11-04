FROM node:22

WORKDIR /app

COPY . .

RUN npm i

RUN npm install -g @angular/cli@16

EXPOSE 4200

CMD ["ng", "serve", "--host", "0.0.0.0"]
