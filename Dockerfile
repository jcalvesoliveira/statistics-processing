FROM grpc/python:1.4

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./main.py /usr/src/app/main.py
COPY ./server /usr/src/app/server

EXPOSE 50050

CMD ["python", "main.py"]
