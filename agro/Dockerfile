
FROM python:3.12.4-slim

WORKDIR /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
#CMD [ "daphne","-b","0.0.0.0","-p 3000","pilar_care.asgi:application"]
