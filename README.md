![DDOS](https://www.cloudflare.com/img/learning/ddos/what-is-a-ddos-botnet/ddos-botnet-attack-cropped.png)
---

# DDOS-Telegram-BOT

## Overview

This Python script implements an enhanced DDoS (Distributed Denial of Service) attack bot using the Ping of Death method. The bot utilizes the `telebot` library for Telegram integration and executes DDoS attacks via the command-line `ping` utility.

## Features

- Accepts target IP addresses or URLs from users via Telegram messaging.
- Initiates DDoS attacks using the Ping of Death method to overwhelm the target with ICMP echo requests.
- Implements error handling and reporting for better monitoring and feedback.
- Provides a user-friendly interface via Telegram bot commands.

## Prerequisites

- Python 3.x installed on your system.
- Telegram API token for bot authentication.
- A Telegram account to interact with the bot.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Mustafa1p/DDOS-Telegram-BOT.git
    ```

2. Obtain your Telegram API token and replace `YOUR_TOKEN_HERE` in the script with your actual token.

3. Set your admin chat ID in the `ADMIN_CHAT_ID` variable to receive error notifications.

## Usage

1. Start the bot by running the script:

    ```bash
    python ddos.py
    ```

2. Open Telegram and start a chat with the bot. Use the `/start` command to initiate the bot and follow the instructions to specify the target IP address or URL.

3. The bot will initiate the DDoS attack using the Ping of Death method upon receiving the target information.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README further to include additional information or formatting as needed.
Developer By MUSTAFA IP 
