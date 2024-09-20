
FROM python:3.12.4-slim

WORKDIR /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000
ARG LOAD_MOCK_DATA=false
CMD ["sh", "-c", "python manage.py migrate && if [ $LOAD_MOCK_DATA = true ]; then python manage.py load_mock_data; fi && python manage.py runserver 0.0.0.0:8000"]

#CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
