import subprocess
import telepot

TELEGRAM_BOT_TOKEN = 'put_your_own'
TELEGRAM_CHAT_ID = 'put_your_own'
IP_LIST_FILE = 'ips.txt'

def send_telegram_message(message):
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    bot.sendMessage(TELEGRAM_CHAT_ID, message)

def ping_ip(ip, alias):
    command = ['ping', '-c', '1', ip]  # Change parameters if using Windows
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
        send_telegram_message(f'✅ {alias} ({ip}) Còn sống. ')
    except subprocess.CalledProcessError as e:
        send_telegram_message(f'🔴 {alias} ({ip}) Ngủm rồi. Error: {e.output.decode()}')

def main():
    with open(IP_LIST_FILE, 'r') as file:
        ip_list = file.read().splitlines()

    for entry in ip_list:
        alias, ip = entry.split(',')
        ping_ip(ip.strip(), alias.strip())

if __name__ == '__main__':
    main()


