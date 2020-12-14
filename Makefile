SHELL := bash

.PHONY: build help generate-proto build-server

PROTO_DIR = ./protos/generated

build: 
	docker build -t statistics-processing .

run:
	docker run --rm -p 50050:50050 statistics-processing

test:
	python -m unittest

generate-proto:
	python -m grpc_tools.protoc -I . --python_out=./ --grpc_python_out=./ server/protos/proto/statistics_processing.proto
