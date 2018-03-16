#!/bin/bash

/etc/init.d/syslog-ng restart
nginx -g "daemon off;"
