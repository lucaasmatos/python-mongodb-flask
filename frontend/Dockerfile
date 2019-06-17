FROM python:3
LABEL maintainer Lucas "lucas.matos.silva1@hotmail.com"

COPY . /app
WORKDIR /app
RUN pip install -r requirements
CMD ["/bin/bash", "-c", "python start.py"]
