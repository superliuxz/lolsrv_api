FROM python:3.6.6-alpine

EXPOSE 10101

RUN apk add --no-cache \
    musl-dev \
    python3-dev \
    gcc \
    postgresql-dev \
    supervisor \
    nginx

# Nginx
RUN rm -rf /etc/nginx/sites-enabled /etc/nginx/sites-available
RUN mkdir /run/nginx /etc/nginx/sites-enabled /etc/nginx/sites-available
COPY conf/nginx/nginx.conf /etc/nginx/
COPY conf/nginx/sites-available/app.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf

# supervisor
RUN mkdir -p /etc/supervisor /var/log/supervisor
COPY conf/supervisor /etc/supervisor/

WORKDIR /app
RUN mkdir -p /app/lolsrv_api
COPY lolsrv_api /app/lolsrv_api
COPY manage.py /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]