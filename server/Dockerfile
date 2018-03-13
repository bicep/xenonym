FROM nginx
RUN apt-get update \
    && apt-get install -y syslog-ng-core
COPY syslog-ng.conf /etc/syslog-ng/syslog-ng.conf
COPY nginx.conf /etc/nginx/nginx.conf
# CMD ["/etc/init.d/syslog-ng", "restart"]