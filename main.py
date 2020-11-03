import requests
import json



def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization' : 'UQWEszbClhvNcL9KgAxr8m3BY4XyjRMTpkuV2PdGIefatnD7O5Qnt6ANYkUvVsyLz4aOWGKhD5bHuCZg',
        'sender_id' : 'FSTSMS'
        'message' :message,
        'language' : 'english',
        'route': 'p',
        'numbers':number
    }
    response = requests.get(url,params=params)
    dic = response.json()
    print(dic)

send_sms("80059xxxxxx","Hello there")