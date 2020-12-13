SHELL := bash

.PHONY: build help generate-proto build-server

PROTO_DIR = ./protos/generated

build: 
	docker build -t statistics-processing .

run:
	docker run --rm -p 50050:50050 statistics-processing

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
