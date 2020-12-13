#!/bin/env bash

for proto_file in server/protos/proto/*.proto; do
    echo "Generating gRPC code for ${proto_file}"
    python -m grpc_tools.protoc -I . --python_out=./ --grpc_python_out=./ ${proto_file}
done
