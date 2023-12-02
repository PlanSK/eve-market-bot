FROM python:3.11.6-alpine

WORKDIR /bot_app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./eve_market_bot/ eve_market_bot/
COPY ./main.py .

CMD [ "python", "./main.py" ]
