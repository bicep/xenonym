FROM balabit/syslog-ng
COPY syslog-ng.conf /etc/syslog-ng/syslog-ng.conf
COPY logger.py /logger.py
# Set the python path to the current working directory
# so that syslog-ng python has access to the logger file
ENV PYTHONPATH="/:$PYTHONPATH:$PWD"
EXPOSE 601:601/tcp
CMD ["-edv"]
