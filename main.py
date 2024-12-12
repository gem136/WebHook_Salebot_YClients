import time

def send_inline_buttons_function():
    # Получаем текущее время (в секундах с эпохи)
    current_time = time.time()

    # Функция для преобразования времени в формат dd.mm
    def format_date(timestamp):
        return time.strftime('%d.%m', time.localtime(timestamp))

    # Генерация дат
    today = format_date(current_time)
    tomorrow = format_date(current_time + 86400)  # 86400 секунд = 1 день
    day_after_tomorrow = format_date(current_time + 2 * 86400)  # 2 дня

    # Формируем структуру кнопок
    buttons = {
        "inline_keyboard": [
            [
                {"text": today, "callback_data": "сегодня"},
                {"text": tomorrow, "callback_data": "завтра"},
                {"text": day_after_tomorrow, "callback_data": "послезавтра"}
            ]
        ]
    }
    print(buttons)

    return buttons
