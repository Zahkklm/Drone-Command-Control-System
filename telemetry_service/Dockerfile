FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["daphne", "-b", "0.0.0.0", "-p", "8001", "telemetry_service.asgi:application"]