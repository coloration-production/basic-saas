# build front-end
FROM node:14-alpine as build

WORKDIR /app

ADD . /app

RUN npm config set registry https://registry.npm.taobao.org

RUN npm install

RUN npm run build:docker

RUN rm -rf ./node_modules

# serve front-end bundle project

FROM nginx:stable-alpine

COPY --from=build /app/dist /bin/www

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]