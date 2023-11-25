import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import socket
import ssl

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Зчитати налаштування з файлу .env
from dotenv import load_dotenv
load_dotenv()

# Встановити параметри підключення
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
if EMAIL_PORT is None:
    logger.error("ERROR: EMAIL_PORT не вказано в .env файлі.")
    exit()
else:
    EMAIL_PORT = int(EMAIL_PORT)

EMAIL_STARTTLS = os.getenv("EMAIL_STARTTLS") == "false"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL") == "true"
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS") == "true"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

# Логування параметрів
logger.info(f"EMAIL_HOST: {EMAIL_HOST}")
logger.info(f"EMAIL_PORT: {EMAIL_PORT}")
# Додайте інші параметри за необхідності

# Перевірка доступності порту
def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout in seconds

    try:
        sock.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

# Логування доступності порту
if is_port_open(EMAIL_HOST, EMAIL_PORT):
    logger.info(f"Порт {EMAIL_PORT} на {EMAIL_HOST} доступний.")
else:
    logger.error(f"Порт {EMAIL_PORT} на {EMAIL_HOST} недоступний.")
    exit()

# Створення тестового листа
subject = "Тестовий лист"
message = "Це тестовий лист від Django."
from_email = DEFAULT_FROM_EMAIL
to = ["sb4mymail@gmail.com"]

# Створення об'єкта MIMEMultipart
msg = MIMEMultipart()
msg.attach(MIMEText(message, 'plain'))

# Налаштування параметрів листа
msg['From'] = from_email
msg['To'] = ", ".join(to)
msg['Subject'] = subject

# Підключення до сервера та відправлення листа
try:
    logger.info(f'Підключення до SMTP-сервера: {EMAIL_HOST}:{EMAIL_PORT}')
    logger.info(f'Логін: {EMAIL_HOST_USER}, Пароль: {EMAIL_HOST_PASSWORD}')

    if EMAIL_USE_SSL:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=context) as server:
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(from_email, to, msg.as_string())
    else:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            if EMAIL_STARTTLS:
                server.starttls()

            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(from_email, to, msg.as_string())

    logger.info('Тестовий лист відправлено успішно.')
except Exception as e:
    logger.error(f'Помилка відправлення листа: {e}')

