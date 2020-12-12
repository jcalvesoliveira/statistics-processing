FROM grpc/python:1.4

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN python -m grpc_tools.protoc -I . --python_out=./server/proto --grpc_python_out=./server/proto protos/proto/statistics_processing.proto

EXPOSE 50050

CMD ["python", "main.py"]
