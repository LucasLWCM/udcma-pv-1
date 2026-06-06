FROM nginx:alpine

COPY output/index.html /usr/share/nginx/html/index.html
COPY img/ /usr/share/nginx/html/img/

RUN sed -i 's|\.\./img/|img/|g' /usr/share/nginx/html/index.html

EXPOSE 80
