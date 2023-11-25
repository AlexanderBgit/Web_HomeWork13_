from dotenv import dotenv_values

# Зчитати значення та типи з файлу .env
env_vars = dotenv_values(".env")
# env_vars = dotenv_values("D:/PyCoreHw/Py/WebHw13/hw13_10_2/hw_improv/.env")

# Вивести значення та типи параметрів
for key, value in env_vars.items():
    print(f"{key}: {value} (тип: {type(value)})")



import configparser
from pathlib import Path

# Шлях до файлу settings.py
settings_file_path = "D:/PyCoreHw/Py/WebHw13/hw13_10_2/hw_improv/settings.py"

# Читаємо вміст файлу
with open(settings_file_path, 'r') as file:
    lines = file.readlines()

# Знаходимо рядок, що містить потрібне значення
for line in lines:
    if line.startswith("DATABASES"):
        # Тут ви можете додатково обробити рядок, витягнути значення тощо
        print(line)

