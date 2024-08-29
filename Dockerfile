FROM python:3.11.2

COPY . .

RUN pip install pyparsing
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD python bot_runner.py