FROM python:3.11

RUN mkdir /telegrambot

WORKDIR /telegrambot

COPY requirements.txt /telegrambot

RUN pip install pyparsing
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY . /bot

CMD [ "python", "./bot.py" ]
