FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3-pip

COPY ./ ./app
WORKDIR ./app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
