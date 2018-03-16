#!/bin/sh

while true
do 
  curl --silent server:80 > dev/null
  sleep 5
done
