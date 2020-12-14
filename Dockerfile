FROM grpc/python:1.4-onbuild

WORKDIR /usr/src/app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY main.py ./
COPY server ./server

RUN python -m grpc_tools.protoc -I . --python_out=./ --grpc_python_out=./ server/protos/proto/statistics_processing.proto

# Downloading grpc_health_probe for K8s readinessProbe and livenessProbe
RUN GRPC_HEALTH_PROBE_VERSION=v0.3.1 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

EXPOSE 50050

CMD ["python", "./main.py"]
