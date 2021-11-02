FROM python:3.8-slim-buster

WORKDIR /prueba_haulmer

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app app
COPY prueba_haulmer.py prueba_haulmer.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
