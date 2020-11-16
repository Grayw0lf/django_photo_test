# Получаем официальный имидж
FROM python:3


# Устанавливаем рабочую директорию
WORKDIR /usr/src/djangophoto

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/djangophoto/
RUN pip install -r requirements.txt

# Копируем entrypoint.sh
COPY ./entrypoint.sh /usr/src/djangophoto/

# Копируем проект
COPY ./ /usr/src/djangophoto/

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/djangophoto/entrypoint.sh"]