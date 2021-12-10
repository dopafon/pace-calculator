FROM python:3.9-slim
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY webapp/ /webapp
COPY run.py /
ENTRYPOINT [ "python" ]
#WORKDIR /webapp
CMD [ "run.py" ]
