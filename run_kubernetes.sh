#!/usr/bin/env bash

dockerpath=walaaelgenidy/devtask:latest

# Run the Docker Hub container with kubernetes
kubectl run devtask\
    --generator=run-pod/v1\
    --image=$dockerpath\
    --port=8000 --labels app=DevTask

# List kubernetes pods
kubectl get pods

# Forward the container port to a host
kubectl port-forward devtask 8000:8080