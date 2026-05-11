
import requests
import time

TELEGRAM_TOKEN = "8609177446:AAGrqMJfSOUwd2kXV50rXHQEj0nOBGvioO0"
TELEGRAM_CHAT_ID = "5213653667"

def send_telegram(message):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)

def test_alert():

    message = """
🚨 BOT CONECTADO COM SUCESSO

Seu bot de pressão ofensiva está funcionando.

Exemplo de alerta:

Manchester City x Fulham
64'
Finalizações: 12
Últimos 10 min: 4
Escanteios: 6

Over 13.5 Finalizações @1.82
"""

    send_telegram(message)

if __name__ == "__main__":

    print("Enviando alerta teste...")
    test_alert()
    print("Mensagem enviada.")
