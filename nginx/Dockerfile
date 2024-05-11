FROM nginx:latest

RUN apt-get -y update
RUN apt-get -y install vim nginx

RUN if ! id -u nginx &>/dev/null; then useradd -r nginx; fi

#RUN mkdir /etc/nginx/html
#COPY nginx.conf /etc/nginx/nginx.conf
#COPY html/ /etc/nginx/html

CMD ["nginx", "-g", "daemon off;"]