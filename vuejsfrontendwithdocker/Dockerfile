FROM node:lts-alpine as frontend-build

WORKDIR /vuejsapp

COPY ./vuejsfrontend .

RUN npm install

EXPOSE 8080

CMD [ "npm", "run", "serve" ]
