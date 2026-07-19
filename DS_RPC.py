import time
from pypresence import Presence

# Сюда вставляешь свой скопированный Application ID
client_id = "1509256034169126992"

# Подключаемся к Дискорду
RPC = Presence(client_id)
RPC.connect()

print("Статус активен, троляканье = true")

# Настройка того, что будет написано в статусе
RPC.update(
    state="tg : @qvertick",        # Нижняя строчка текста
    details="Альтухи Краков ГАЗ знакомиться",            # Верхняя строчка текста
    start=time.time(),                  # Включает счетчик времени
    large_image="logo",                 # Имя картинки из Art Assets
    large_text="<3",       # Текст при наведении на картинку
    buttons=[
        {"label": "Мой Гитхаб", "url": "https://github.com/qvertick"}
    ]
)

# Цикл, чтобы скрипт не закрывался и статус держался
while True:
    time.sleep(15)
