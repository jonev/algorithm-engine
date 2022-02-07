#! /bin/bash
# Finding the container name
containername=$(docker ps | grep 'vsc-worker' | awk '{print $1}')
echo "Connecting: $containername"
networkname=$(docker network ls --format "{{.Name}}" | grep '^algorithm-engine_default')
echo "to: $networkname"
docker network connect $networkname $containername
