# VK-TELEGRAM-DIALOG-BOT

��������� ���������� ����� ��� ��������� � Telegram �� ����� Python/Dialogflow

### ��� ����������

Python3 ������ ���� ��� ����������. ����� ����������� pip (��� pip3, ���� �������� � Python2) ��� ��������� ������������:
```
pip install -r requirements.txt
```

### ����� �������� 
##### 1. ������ ���������, � ������� ����� �������������� ��� ���������-���.

��������� ���� �������� ���������:
<img src="https://dvmn.org/media/screenshot_from_2019-04-29_20-15-54.png">

##### 2 .�������� ���� �� ������ � ���� ������� � API� - ������� ���� �������:
<img src="https://dvmn.org/filer/canonical/1556554255/101/">
������ ���� �������� � ���������� `VK_GROUP_ACCESS_KEY` ����� `.env` �������:
```
VK_GROUP_ACCESS_KEY='YOUR_VK_GROUP_ACCESS_KEY'
```

##### 3. ������� ��������� ���-����. 

���������� �� ����������� ���� � ��������� ������ �����: https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/ ��� �����: https://habr.com/ru/post/262247/.
������: ������ �������� � ��������� ���� @BotFather � �������� ��� �����������. 
���������� ����� ��������� � ���������� `TG_BOT_TOKEN` ����� `.env` �������:

```
TG_BOT_TOKEN='YOUR_TELEGRAM_BOT_TOKEN'
```
##### 4. �������� ID ������ ���� � ���������.

��� ����� ���������� �������� ���� `@userinfobot`.
���������� ID ��������� � ���������� `SESSION_ID` ����� `.env` �������:
```
SESSION_ID='YOUR_TELEGRAM_CHAT_ID'
```
##### 5. �������� ������� � Dialogflow: https://dialogflow.cloud.google.com/#/login
������ �������� �������� �� ������:
'Use the service account key file in your environment'
���� �� ���������� ����� ������� � ���������� GOOGLE_APPLICATION_CREDENTIALS
`` ����� `.env` �������:
```
GOOGLE_APPLICATION_CREDENTIALS='PATH_TO_YOUR_CREDENTIALS_JSON_FILE'
```

##### 6. �������� ������, ������ � ������� ��� ���� � Dialogflow 
��� ������� ������ ������� �����: https://cloud.google.com/dialogflow/es/docs/quick/setup
<img src="https://dvmn.org/media/project.png">
������������� ������� ������� � ���������� `DIALOG_FLOW_PROJECT_ID` ����� `.env` �������:
```
DIALOG_FLOW_PROJECT_ID='YOUR_DIALOGFLOW_PROJECT_ID'_TOKEN'
```
������ ��������������: 
`moonlit-dynamo-211973`
����� ���������� ������� "������" � Dialogflow:
������ � ��� ���-�� ����� ������ � Telegram, ������ � DialogFlow. ����� ������������ DialogFlow, ����� ������� ����, �.�. ������.
https://cloud.google.com/dialogflow/docs/quick/build-agent
�� ����������� �������� ������ �� �������� �������� �� ����������� ��������:
<img src="https://dvmn.org/media/agent.png">
����� ����������� Intents ��� ����, ��������� ��������� ��� ���� �����������.
��� ����� Intents � Dialoflow ������� �����: https://cloud.google.com/dialogflow/es/docs/intents-overview
� ������ ����������� � �������� ������� ��� ����������� ��������  ���������� �������� � �������� �������.

### ������ ������
������, ����� �� ��������� ��� ��������� ���������� ��������� ����� ���������� � ������� ����� ����� � ������� ������.
��� ����, ����� ������� �������� ������� ��� ������ Dialogflow, ����������� ��������� ������� � ���������:
```  
$python dialogflow_learner.py
```  

� �������� ������ (��� ������) ������� ����� ����������� ������� ����������� ������ �� ���������:
��� ���������-����:
```  
$python telegram_bot.py
```  
� ��� ���� ���������, ��������������:
```  
$python vk_bot.py
```
##### ������������
�� ��������� ����� ������������ �������� ����� �������, ��� ��� root-���� ������� ��������������� � ��������.
��������� �� � �������� �����, � ����� �� ������� �������� � ��� ��������-���.
��� ������������ ������������ ������ `logging`.
������������ �������� �����: https://docs.python.org/3/library/logging.html
��������� ������������ ��������� � �����:
`log_settings.py` 


### ������� ������ �����
������ ������ ���� � ��������:

<img src="https://s7.gifyu.com/images/TG66bcf8bd144dfaf0.gif">

������ ������ ���� ���������:

<img src="https://s7.gifyu.com/images/VK1f77aedc12b4d83f.gif">

#### ������ �� ������������ �������� ����:

���������: 
https://vk.com/im?sel=-212362400

��������: 
https://t.me/game_of_verbs_dvmn_bot

### ������� ������ � ������� Heroku
�������������� ���. ��� ����� �������� � ��������������� �� ����� ������� (��� ������� ��������). 
����� ���������� ��� ��� �� ������� ��������� ����� ������������ ������ Heroku https://heroku.com. ���������� �� ������ �����: https://ru.stackoverflow.com/questions/896229/%D0%94%D0%B5%D0%BF%D0%BB%D0%BE%D0%B9-%D0%B1%D0%BE%D1%82%D0%B0-%D0%BD%D0%B0-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%B5-heroku ��� ����� (���������� ��� ��-���������� �� Python, �� ��� �������� ����������): https://blog.disonds.com/2017/03/20/python-bot-dlya-vk-na-heroku/ 
����� ��������, ��� ������� ���������� �� Heroku ����� � ��� ������������� Heroku CLI, �� ��� ����� ������ ������� ��� ����� ����� �����.

������:

������� � ��� ���������� ������������ ������� GitHub https://github.com/;
"���������" ������ ����������� � ���� � �������;
�������������� � Heroku � ������� ���������� �� ���������� ����;
"�����������" ������� ������ GitHub � ������� ������ Heroku;
� �������� ����������� � Deployment Method �� �������� Deploy ������ ���������� � Heroku ��������� GitHub � ��������� ������ �� ������ �����������;
��������� ���� �� �������, ����� ������ connect.

��������, ��� ������ ����� ������� �����������, ��������� � ������ 
`GOOGLE_APPLICATION_CREDENTIALS` 
������������ ����������� ������������ � ������� ����������� �����:
https://stackoverflow.com/questions/47446480/how-to-use-google-api-credentials-json-on-heroku
� ������������ ���������� �������, ����������� �� ������:
https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack

### ���� �������

��� ������� � ��������������� ����� �� ������-����� ��� ���-������������� dvmn.org.