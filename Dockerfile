FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
COPY p0/ /usr/share/nginx/html/p0/
COPY p2/ /usr/share/nginx/html/p2/
COPY p3/ /usr/share/nginx/html/p3/
COPY p5/ /usr/share/nginx/html/p5/
COPY img/ /usr/share/nginx/html/img/

EXPOSE 80
