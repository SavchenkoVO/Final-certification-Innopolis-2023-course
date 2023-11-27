FROM python:3.9.18-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

RUN python3 fill_db.py

EXPOSE 80
CMD flask --app web-app/main.py run --host=0.0.0.0 --port=80