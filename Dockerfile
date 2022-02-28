FROM python:3.8

RUN mkdir -p /bot/src
WORKDIR /bot/src

COPY requirements.txt /bot/requirements.txt
RUN pip install -r /bot/requirements.txt


COPY faq.json /bot/faq.json
COPY src /bot/src

CMD ["sh", "-c",  "python main.py"]
