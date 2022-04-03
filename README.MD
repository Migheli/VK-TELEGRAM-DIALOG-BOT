# VK-TELEGRAM-DIALOG-BOT

Запускаем диалоговых ботов для Вконтакте и Telegram на стеке Python/Dialogflow

### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Перед запуском 
##### 1. Группа Вконтакте, в которой будет использоваться Ваш Вконтакте-бот.

Разрешаем боту отправку сообщений:
<img src="https://dvmn.org/media/screenshot_from_2019-04-29_20-15-54.png">

##### 2 .Получаем ключ от группы в меню “Работа с API” - создать ключ доступа:
<img src="https://dvmn.org/filer/canonical/1556554255/101/">
Данный ключ помещаем в переменную `VK_GROUP_ACCESS_KEY` файла `.env` проекта:
```
VK_GROUP_ACCESS_KEY='YOUR_VK_GROUP_ACCESS_KEY'
```

##### 3. Создаем телеграмм чат-бота. 

Инструкция по регистрации бота и получению токена здесь: https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/ или здесь: https://habr.com/ru/post/262247/.
Кратко: просто напишите в телеграмм боту @BotFather и следуйте его инструкциям. 
Полученный токен сохраните в переменную `TG_BOT_TOKEN` файла `.env` проекта:

```
TG_BOT_TOKEN='YOUR_TELEGRAM_BOT_TOKEN'
```
##### 4. Получите ID Вашего чата в телеграмм.

Для этого достаточно написать боту `@userinfobot`.
Полученный ID сохраните в переменную `SESSION_ID` файла `.env` проекта:
```
SESSION_ID='YOUR_TELEGRAM_CHAT_ID'
```
##### 5. Создайте аккаунт в Dialogflow: https://dialogflow.cloud.google.com/#/login
Особое внимание обратите на раздел:
'Use the service account key file in your environment'
Путь до созданного файла укажите в переменной GOOGLE_APPLICATION_CREDENTIALS
`` файла `.env` проекта:
```
GOOGLE_APPLICATION_CREDENTIALS='PATH_TO_YOUR_CREDENTIALS_JSON_FILE'
```

##### 6. Создайте проект, агента и интенты для него в Dialogflow 
Как создать проект описано здесь: https://cloud.google.com/dialogflow/es/docs/quick/setup
<img src="https://dvmn.org/media/project.png">
Идентификатор проекта внесите в переменную `DIALOG_FLOW_PROJECT_ID` файла `.env` проекта:
```
DIALOG_FLOW_PROJECT_ID='YOUR_DIALOGFLOW_PROJECT_ID'_TOKEN'
```
Пример идентификатора: 
`moonlit-dynamo-211973`
Далее необходимо создать "агента" в Dialogflow:
“Агент” — это что-то вроде “бота” в Telegram, только в DialogFlow. Чтобы пользоваться DialogFlow, нужен местный “бот”, т.е. “агент”.
https://cloud.google.com/dialogflow/docs/quick/build-agent
По результатам создания агента Вы попадете примерно на аналогичную страницу:
<img src="https://dvmn.org/media/agent.png">
Также потребуются Intents для бота, созданные конкретно под Ваши потребности.
Что такое Intents в Dialoflow читайте здесь: https://cloud.google.com/dialogflow/es/docs/intents-overview
В данном репозитории в качестве примера уже реализовано создание  нескольких интентов в качестве примера.

### Начало работы
Теперь, когда мы заполнили все требуемые переменные окружения можно приступать к запуску наших ботов в теством режиме.
Для того, чтобы создать тестовые интенты для агента Dialogflow, используйте следующую команду в терминале:
```  
$python dialogflow_learner.py
```  

В тестовом режиме (без деплоя) скрипты ботов запускаются простым выполнением команд из терминала:
для Телеграмм-бота:
```  
$python telegram_bot.py
```  
и для бота Вконтакте, соответственно:
```  
$python vk_bot.py
```
##### Логгирование
По умолчанию режим логгирования настроен таким образом, что все root-логи сыпятся непосредственно в терминал.
Сообщения же о запусках ботов, а также об ошибках приходят в Ваш телеграм-чат.
Для логгирования используется модуль `logging`.
Документация доступна здесь: https://docs.python.org/3/library/logging.html
Настройки логгирования размещены в файле:
`log_settings.py` 


### Примеры работы ботов
Пример работы бота в Телеграм:

<img src="https://s7.gifyu.com/images/TG66bcf8bd144dfaf0.gif">

Пример работы бота Вконтакте:

<img src="https://s7.gifyu.com/images/VK1f77aedc12b4d83f.gif">

#### Ссылки на задеплоенные тестовые боты:

Вконтакте: 
https://vk.com/im?sel=-212362400

Телеграм: 
https://t.me/game_of_verbs_dvmn_bot

### Деплоим проект с помощью Heroku
Необязательный шаг. Бот может работать и непосредственно на Вашем сервере (при наличии такового). 
Чтобы развернуть наш бот на сервере бесплатно можно использовать сервис Heroku https://heroku.com. Инструкция по деплою здесь: https://ru.stackoverflow.com/questions/896229/%D0%94%D0%B5%D0%BF%D0%BB%D0%BE%D0%B9-%D0%B1%D0%BE%D1%82%D0%B0-%D0%BD%D0%B0-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%B5-heroku или здесь (инструкция для ВК-приложений на Python, но все работает аналогично): https://blog.disonds.com/2017/03/20/python-bot-dlya-vk-na-heroku/ 
Важно отметить, что создать приложение на Heroku можно и без использования Heroku CLI, но оно будет крайне полезно для сбора наших логов.

Кратко:

создаем и или используем существующий аккаунт GitHub https://github.com/;
"клонируем" данный репозиторий к себе в аккаунт;
регистрируемся в Heroku и создаем приложение по инструкции выше;
"привязываем" учетную запись GitHub к учетной записи Heroku;
в качестве репозитория в Deployment Method на странице Deploy Вашего приложения в Heroku указываем GitHub и добавляем ссылку на данный репозиторий;
запускаем бота на сервере, нажав кнопку connect.

Внимание, при деплое ботов имеется особенность, связанная с ключом 
`GOOGLE_APPLICATION_CREDENTIALS` 
Настоятельно рекомендуем ознакомиться с краткой инструкцией здесь:
https://stackoverflow.com/questions/47446480/how-to-use-google-api-credentials-json-on-heroku
и использовать актуальный билдпак, размещенный по адресу:
https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.