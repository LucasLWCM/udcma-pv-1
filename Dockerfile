FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
COPY p0/ /usr/share/nginx/html/p0/
COPY p2/ /usr/share/nginx/html/p2/
COPY p3/ /usr/share/nginx/html/p3/
COPY p4/ /usr/share/nginx/html/p4/
COPY p5/ /usr/share/nginx/html/p5/
COPY p6/ /usr/share/nginx/html/p6/
COPY p7/ /usr/share/nginx/html/p7/
COPY p8/ /usr/share/nginx/html/p8/
COPY p9/ /usr/share/nginx/html/p9/
COPY pe00/ /usr/share/nginx/html/pe00/
COPY principal/ /usr/share/nginx/html/principal/
COPY obrigado/ /usr/share/nginx/html/obrigado/
COPY img/ /usr/share/nginx/html/img/

EXPOSE 80
