#!/bin/bash

echo "Waiting for Zookeeper to start..."

# Wait for Zookeeper to start by checking if the port 2181 is open
while ! nc -z zookeeper 2181; do   
  sleep 0.1 # wait for 1/10 of the second before checking again
done

echo "Zookeeper started."
