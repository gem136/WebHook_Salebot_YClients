from datetime import datetime, timedelta
import json

# Генерация дат
today = datetime.now().strftime('%d.%m')
tomorrow = (datetime.now() + timedelta(days=1)).strftime('%d.%m')
day_after_tomorrow = (datetime.now() + timedelta(days=2)).strftime('%d.%m')

# Создаем JSON для inline-кнопок
buttons = [
    {"text": today, "callback_data": "сегодня"},
    {"text": tomorrow, "callback_data": "завтра"},
    {"text": day_after_tomorrow, "callback_data": "послезавтра"}
]

# Возвращаем JSON в формате строки
dynamic_buttons = json.dumps(buttons)
