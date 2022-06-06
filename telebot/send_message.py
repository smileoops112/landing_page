import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = ' https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    a = text.find('{')
    b = text.find('}')
    c = text.rfind('{')
    d = text.rfind('}')
    text_1 = text[0:a]
    text_2 = text[b+1:c]
    text_3 = text[d:-1]
    text_s = text_1 + tg_name + text_2 + tg_phone +text_3
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_s
    })

