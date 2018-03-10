FROM ubuntu
RUN apt-get update \
    && apt-get install -y curl
ADD entrypoint.sh /entrypoint.sh
CMD [ "bash", "/entrypoint.sh" ]