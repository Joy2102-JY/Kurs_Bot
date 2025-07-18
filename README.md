# Telegram Bot — Учебный проект

Простой Telegram-бот с reply и inline кнопками.

## 📌 Команды

- `/start` — приветствие и reply-кнопки
- `/help` — справка
- `/menu` — inline-кнопки:
  - 🔗 Открыть сайт: [python.org](https://www.python.org)
  - 🔘 Нажми меня! — ответ: "Ты нажал кнопку!"

## 📁 Структура проекта
telegram_bot/ ├── bot.py # основной код └── .env # переменная TELEGRAM_TOKEN


## 🚀 Установка

1. Установите зависимости:

```bash
pip install python-telegram-bot python-dotenv
python bot.py
