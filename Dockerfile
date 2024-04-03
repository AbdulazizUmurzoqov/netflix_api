FROM python:3.7

WORKDIR netflix/

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["./script.sh"]