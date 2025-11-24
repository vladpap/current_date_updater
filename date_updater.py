import datetime
from PIL import Image, ImageDraw, ImageFont
import os

def create_date_image(width=400, height=200):
    """Создает PNG с текущей датой и прозрачностью 50%"""
    # Определяем путь к рабочей директории
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "current_date.png")
    
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    
    try:
        font = ImageFont.truetype("arial.ttf", 48)
    except:
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", 48)
        except:
            font = ImageFont.load_default()
    
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
    
    image.save(output_path, "PNG")
    
    # Логируем в файл для отладки
    log_path = os.path.join(script_dir, "date_update.log")
    with open(log_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: Изображение обновлено - {current_date}\n")

if __name__ == "__main__":
    create_date_image()
