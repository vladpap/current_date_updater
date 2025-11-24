import os
import datetime
from PIL import Image, ImageDraw, ImageFont
import time
import schedule

font_size = 72

def create_date_image_small():
    """Маленький шрифт (24px)"""
    create_date_image_custom(font_size=24)

def create_date_image_medium():
    """Средний шрифт (36px)"""
    create_date_image_custom(font_size=36)

def create_date_image_large():
    """Большой шрифт (60px)"""
    create_date_image_custom(font_size=60)


def create_date_image_custom(width=250, height=75, font_size=48):
    """
    Создает PNG изображение с текущей датой белым цветом и черной тенью
    с прозрачностью 50%
    """
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    
    try:
        font = ImageFont.truetype("Andale Mono.ttf", font_size)
        print("Andale Mono.ttf")
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", font_size)
            print("Arial.ttf")
        except:
            font = ImageFont.load_default()
            print("default")
    
    bbox = draw.textbbox((0, 0), current_date, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Цвета с прозрачностью 50%
    shadow_color = (0, 0, 0, 128)
    text_color = (255, 255, 255, 128)
    
    # Тень
    shadow_offset = 2
    draw.text((x + shadow_offset, y + shadow_offset), current_date, 
              font=font, fill=shadow_color)
    
    # Текст
    draw.text((x, y), current_date, font=font, fill=text_color)
    
    image.save("current_date.png", "PNG")
    print(f"Изображение обновлено: {current_date} (размер шрифта: {font_size}px)")
    
    image.save("current_date.png", "PNG")
    print(f"Изображение с улучшенной тенью обновлено: {current_date}")

def update_daily():
    """Функция для ежедневного обновления в 00:01"""
    create_date_image_medium()

def main():
    # Создаем первое изображение при запуске
    create_date_image_medium()
    
    # Настраиваем ежедневное обновление в 00:01
    schedule.every().day.at("00:01").do(update_daily)
    
    print("Сервис запущен. Изображение будет обновляться ежедневно в 00:01")
    print("Для остановки нажмите Ctrl+C")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Проверяем каждую минуту
    except KeyboardInterrupt:
        print("Сервис остановлен")

# Альтернативная версия для Windows (без schedule)
def windows_version():
    """
    Версия для Windows, которая использует планировщик задач
    Запускайте эту функцию через планировщик задач Windows
    """
    create_date_image_medium()

if __name__ == "__main__":
    # Проверяем, хотим ли мы запустить как сервис или однократно
    response = input("Запустить как сервис (s) или создать однократно (o)? ").lower()
    
    if response == 's':
        main()
    elif response == 'b':
        # Опция для версии с улучшенной тенью
        create_date_image_medium()
        print("Изображение с улучшенной тенью создано однократно")
    else:
        create_date_image_medium()
        print("Изображение создано однократно")
