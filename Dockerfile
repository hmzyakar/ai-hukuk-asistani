# Temel imaj olarak Python 3.11'in tam versiyonunu kullanıyoruz.
FROM python:3.11

# Konteyner içindeki çalışma klasörümüzü belirliyoruz.
WORKDIR /app

# Gerekli sistem araçlarını, Node.js/npm'i ve Google Chrome'u kuruyoruz.
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Google Chrome'u kurmak için modern ve güvenli yöntem:
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/google-chrome-stable.gpg
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update && apt-get -y install google-chrome-stable

# --- DEĞİŞİKLİK BURADA BAŞLIYOR ---

# Önce projemizin Python bağımlılıklarını kuruyoruz.
# chromedriver-autoinstaller'ı requirements.txt'ye ekleyeceğiz.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Şimdi, Python'u kullanarak ChromeDriver'ı kuruyoruz.
# Bu, karmaşık ve kırılgan bash komutlarından çok daha sağlam bir yöntemdir.
RUN python -c "import chromedriver_autoinstaller; chromedriver_autoinstaller.install()"

# Claude Code aracını kuruyoruz.
RUN npm install -g @anthropic-ai/claude-code

# Projemizin geri kalan tüm dosyalarını konteynerin içine kopyalıyoruz.
COPY . .