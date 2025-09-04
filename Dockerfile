# 1. Adım: Temel imaj olarak Python 3.11'in hafif bir versiyonunu kullanıyoruz.
FROM python:3.11-slim

# 2. Adım: Konteyner içindeki çalışma klasörümüzü belirliyoruz.
WORKDIR /app

# 3. Adım: Gerekli sistem araçlarını ve Node.js/npm'i kuruyoruz.
# apt-get, Debian/Ubuntu tabanlı sistemlerin paket yöneticisidir.
RUN apt-get update && apt-get install -y --no-install-recommends \
    nodejs \
    npm \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Adım: Claude Code aracını npm ile global olarak kuruyoruz.
RUN npm install -g @anthropic-ai/claude-code

# 5. Adım: Projemizin Python bağımlılıklarını kuruyoruz.
# Önce sadece requirements.txt dosyasını kopyalayıp kuruyoruz.
# Bu, Docker'ın katmanlama (caching) özelliğinden faydalanarak,
# her kod değişikliğinde kütüphaneleri tekrar kurmasını engeller.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Adım: Projemizin geri kalan tüm dosyalarını konteynerin içine kopyalıyoruz.
COPY . .