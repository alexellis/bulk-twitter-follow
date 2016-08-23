FROM python:2.7.12-alpine
USER root

WORKDIR /root/
RUN pip install tweepy

ADD ./app.py ./app.py

CMD ["python", "app.py"]
