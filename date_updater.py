import os
import datetime
from PIL import Image, ImageDraw, ImageFont
import time
import schedule

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
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), current_date, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Цвета с прозрачностью 50%
    shadow_color = (0, 0, 0, 200)
    text_color = (255, 255, 255, 255)
    
    # Тень
    shadow_offset = 2
    draw.text((x + shadow_offset, y + shadow_offset), current_date, 
              font=font, fill=shadow_color)
    
    # Текст
    draw.text((x, y), current_date, font=font, fill=text_color)
    
    # Сохраняем изображение
    image.save("current_date.png", "PNG")
    
    # Также сохраняем на внешний диск (если нужно)
    try:
        image.save("/Volumes/variag/hires/poleznoe/Watermarks/current_date.png", "PNG")
    except:
        pass
    
    print(f"Изображение обновлено: {current_date} (размер шрифта: {font_size}px)")

def update_daily():
    """Функция для ежедневного обновления в 00:01"""
    create_date_image_custom(font_size=36)  # Средний шрифт

def main():
    # Создаем первое изображение при запуске
    print("Сервис запускается...")
    create_date_image_custom(font_size=36)
    
    # Настраиваем ежедневное обновление в 00:01
    schedule.every().day.at("00:01").do(update_daily)
    
    print("Сервис запущен. Изображение будет обновляться ежедневно в 00:01")
    print("Для остановки нажмите Ctrl+C")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Проверяем каждую минуту
    except KeyboardInterrupt:
        print("\nСервис остановлен")

if __name__ == "__main__":
    # Всегда запускаем как сервис
    main()
