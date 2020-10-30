## Telegram бот для получения курса биткоина в рублях, долларах и евро

### Порядок развертывания бота

Клонируем проект
```
git clone https://github.com/sanyapalmero/bitcoin-course-telegram-bot.git
```

Переходим в папку бота
```
cd bitcoin-course-telegram-bot/
```

Создаем виртуальное окружение (вместо python3 может быть py)
```
python3 -m venv venv
```

Активируем виртуальное окружение, чтобы все зависимости установились в папку venv
```
source venv/Scripts/activate (на Windows)
source venv/bin/activate (на Linux)
```

Устанавливаем зависимости
```
pip install -r requirements.txt
```

В папке проекта создаем файл config.py и указываем токен бота
```
token = ""
```

Запускаем бота
```
python3 bot.py
```
