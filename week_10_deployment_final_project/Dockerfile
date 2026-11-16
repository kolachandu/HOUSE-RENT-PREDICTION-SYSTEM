FROM python:3.12-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python src/preprocessing/clean_data.py

EXPOSE 8000
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
