#!/bin/sh

sleep 20 # give Elasticsearch time to start up
while true
do 
  curl --silent server:80 > dev/null
  sleep 5
done
