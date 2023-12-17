# Python tabanlı resmi Docker imajını kullan
FROM python:latest

# Docker içinde çalışacak dizini ayarla
WORKDIR /app

# Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Şu anki dizindeki kodları Docker içine kopyala
COPY . /app

# Flask uygulamasını 5000 portunda çalıştır
EXPOSE 5000
CMD ["python", "main.py"]
