import qrcode
from PIL import Image

# Ваш URL для веб-сайта
url = "https://altaircom.ru/"

# Путь к изображению, которое вы хотите добавить в QR-код
image_path = "qrlogo.jpg"

# Создание объекта QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=4,
)

# Добавление URL в объект QRCode
qr.add_data(url)
qr.make(fit=True)

# Создание изображения QR-кода с использованием библиотеки Pillow
img = qr.make_image(fill_color="black", back_color="white")

# Открытие изображения, которое вы хотите добавить в QR-код
icon = Image.open(image_path)

# Расчет координат для центрирования изображения
pos = ((img.size[0] - icon.size[0]) // 2, (img.size[1] - icon.size[1]) // 2)

# Наложение изображения на QR-код
img.paste(icon, pos)

# Сохранение изображения в файл (в формате PNG)
img.save("qrcode_with_image.png")
