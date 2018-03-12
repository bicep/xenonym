FROM ubuntu
RUN apt-get update \
    && apt-get install -y curl
COPY entrypoint.sh /entrypoint.sh
CMD [ "bash", "/entrypoint.sh" ]
