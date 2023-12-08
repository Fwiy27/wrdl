FROM python:3.10-slim

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install colorama --trusted-host pypi.org --trusted-host files.pythonhosted.org pip setuptools

CMD [ "python", "main.py" ]