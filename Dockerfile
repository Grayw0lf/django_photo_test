# Получаем официальный имидж
FROM python:3


# Устанавливаем рабочую директорию
WORKDIR /apps

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY apps/requirements.txt .
RUN pip install -r requirements.txt

# Копируем проект
COPY apps .