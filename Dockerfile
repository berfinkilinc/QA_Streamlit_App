FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY .streamlit/config.toml .streamlit/config.toml
COPY Data/df_merged.csv Data/df_merged.csv
COPY main.py .
COPY my-embeddings.zip .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]