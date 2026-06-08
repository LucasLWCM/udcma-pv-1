FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
COPY p2/ /usr/share/nginx/html/p2/
COPY img/ /usr/share/nginx/html/img/

EXPOSE 80
