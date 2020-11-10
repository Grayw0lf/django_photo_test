# Получаем официальный имидж
FROM python:3


# Устанавливаем рабочую директорию
WORKDIR /djangophoto

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Копируем проект
COPY . .