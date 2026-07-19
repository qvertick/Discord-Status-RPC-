import time
import sys
import os
from pypresence import Presence

# Красивое текстовое лого в стиле neofetch
DISCORD_LOGO = """
        @@@@@@@@        qvertick@rpc
      @@@@@@@@@@@@      ------------
    @@@@  @@@@  @@@@    OS: Discord Status RPC
   @@@@@@@@@@@@@@@@@@   Status: Active 🎮
  @@@@@@@@@@@@@@@@@@@@  Target: Custom Rich Presence
  @@@@  @@@@@@@@  @@@@  Engine: pypresence (Python)
  @@@@@@        @@@@@@  
    @@@@@@@@@@@@@@@@    
"""

# Очистка консоли перед выводом (работает и на Windows, и на Linux)
os.system('cls' if os.name == 'nt' else 'clear')
print(DISCORD_LOGO)

client_id = "1509256034169126992"
RPC = Presence(client_id)

print(" -> Ожидание подключения к Discord...")
while True:
    try:
        RPC.connect()
        break
    except Exception:
        time.sleep(5)

print(" -> Успешно подключено! Статус обновлен.")

# Стартовое время, чтобы таймер не сбрасывался при каждом обновлении
start_time = time.time()

# Цикл поддержания статуса с проверкой активности Discord
while True:
    try:
        RPC.update(
            state="tg : @qvertick",
            details="I use Arch btw",
            start=start_time,
            large_image="logo",
            large_text="<3",
            buttons=[{"label": "Мой Гитхаб", "url": "https://github.com/qvertick"}]
        )
        time.sleep(15)
    except Exception:
        print("\n[!] Discord был закрыт. Завершение работы скрипта...")
        time.sleep(2)
        sys.exit()
