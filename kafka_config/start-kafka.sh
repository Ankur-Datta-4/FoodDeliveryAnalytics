#!/bin/bash

# Start Kafka server
nohup kafka/bin/kafka-server-start.sh kafka/config/server.properties > /dev/null 2>&1 &
