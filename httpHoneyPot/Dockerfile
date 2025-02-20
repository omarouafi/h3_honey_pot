FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002 5003

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python login.py & sleep 2 && python fakeLogin.py"]
