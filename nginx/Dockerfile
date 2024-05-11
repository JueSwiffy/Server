FROM nginx:latest

RUN apt-get -y update \
    && apt-get -y install vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && if ! getent passwd nginx >/dev/null; then useradd -r nginx; fi

CMD ["nginx", "-g", "daemon off;"]
