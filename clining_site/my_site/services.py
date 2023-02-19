import requests
from django.conf import settings


TOKEN = settings.TELEGRAM_BOT_TOKEN
chat_id = settings.TELEGRAM_CHAT_ID

   
def main(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

    return (requests.get(url).json()) # this sends the message to chanel







        
    
