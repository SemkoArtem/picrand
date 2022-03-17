FROM python:3.9
WORKDIR /usr/src/picrand

COPY picsrandeomly.py parse_reactor.py main.py config_pics.json ./

RUN pip install pyTelegramBotAPI telebot vk bs4

CMD python3 main.py