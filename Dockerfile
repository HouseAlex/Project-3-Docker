FROM python:3.9

WORKDIR /home

RUN mkdir data

RUN mkdir output

COPY IF.txt data

COPY Limerick-1.txt data

COPY FileRead.py .

RUN python FileRead.py

RUN cat output/result.txt