import requests
from win10toast import ToastNotifier
import time

# Armazenar o meu IP atual
Meu_ip = requests.get('https://api.ipify.org').text

def show_notification(novo_ip):
    toaster = ToastNotifier()
    toaster.show_toast("IP Público Alterado",
                       f"O novo endereço IP público é: {novo_ip}",
                       duration=10)

def check_ip():
    global Meu_ip

    # Obter o  novo IP
    resposta = requests.get('https://api.ipify.org').text
    novo_ip = resposta.strip()

    # Verificar se o IP foi alterado
    if novo_ip != Meu_ip:
        if Meu_ip is not None:
            show_notification(novo_ip)
        Meu_ip = novo_ip

# Intervalo de verificação (em segundos)
interval = 1800  # 30 Min

# Loop para verificar periodicamente o IP
while True:
    check_ip()
    time.sleep(interval)
