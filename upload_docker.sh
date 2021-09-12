#!/usr/bin/env bash
# Assumes that an image is built via `run_docker.sh`
# Create dockerpath
dockerpath=walaaelgenidy/devtask:latest
 
# Authenticate & tag
docker tag devtask walaaelgenidy/devtask
echo "Docker ID and Image: $dockerpath"

#Push image to a docker repository
docker push walaaelgenidy/devtask:latest