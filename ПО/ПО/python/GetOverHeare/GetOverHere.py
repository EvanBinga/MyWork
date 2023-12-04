



 import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Базовый URL
base_url = "https://wgspb.ru/catalog/electronic-modules/modular-embedded/"

# Введите желаемое количество страниц
num_pages = 5 # Измените на нужное количество страниц

# Попытаемся открыть существующий XML-файл, если он существует
try:
    tree = ET.parse("products.xml")
    root = tree.getroot()
except FileNotFoundError:
    # Если файл не существует, создаем новый корневой элемент
    root = ET.Element("products")

# Функция для обработки страницы и добавления данных в XML
def process_page(url):
    # Отправляем GET-запрос на сайт
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Разбираем HTML-страницу с помощью Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Найдите все элементы с классом "shop-item-single"
        product_blocks = soup.find_all(class_="shop-item-single")

        # Обрабатываем данные о товарах и добавляем их в XML
        for product_block in product_blocks:
            product_element = ET.SubElement(root, "product")

            product_name_element = product_block.find(class_="avm-marking")
            product_description_element = product_block.find(class_="avm-description")
            product_quantity_element = product_block.find(class_="avm-column-content")
            product_availability_element = product_block.find(class_="avm-availability")
            product_price_element = product_block.find(class_="avm-shop-item-price--current")

            if product_name_element:
                product_name = product_name_element.text.strip()
                ET.SubElement(product_element, "name").text = product_name

            if product_description_element:
                product_description = product_description_element.text.strip()
                ET.SubElement(product_element, "description").text = product_description

            if product_quantity_element:
                product_quantity = product_quantity_element.text.strip()
                ET.SubElement(product_element, "quantity").text = product_quantity

            if product_availability_element:
                product_availability = product_availability_element.text.strip()
                ET.SubElement(product_element, "availability").text = product_availability

            if product_price_element:
                product_price = product_price_element.text.strip()
                ET.SubElement(product_element, "price").text = product_price
    else:
        print(f"Не удалось получить доступ к странице: {url}")

# Обрабатываем каждую страницу из списка
for page_number in range(1, num_pages + 1):
    page_url = f"{base_url}page-{page_number}/"
    print(f"Обработка страницы: {page_url}")
    process_page(page_url)

# Создаем XML-документ и сохраняем его в файл
tree = ET.ElementTree(root)
tree.write("products.xml", encoding="utf-8")

















# import re
# from lxml import etree as ET

# # Открываем файл с данными
# with open('products.xml', 'r', encoding='utf-8') as file:
#     data = file.read()

# # Создаем корневой элемент XML
# root = ET.Element("products")

# # Используем регулярные выражения для извлечения данных о продуктах
# matches = re.findall(r'<name>(.*?)</name><description>(.*?)</description><quantity>(.*?)</quantity><price>(.*?)</price>', data)

# # Создаем элементы для каждого продукта и добавляем их в корень
# for match in matches:
#     product_element = ET.Element("product")

#     name = ET.SubElement(product_element, "name")
#     name.text = match[0]

#     description = ET.SubElement(product_element, "description")
#     description.text = match[1]

#     quantity = ET.SubElement(product_element, "quantity")
#     quantity.text = match[2]

#     price = ET.SubElement(product_element, "price")
#     price.text = match[3]

#     root.append(product_element)

# # Создаем XML-документ и сохраняем его в файл с разметкой
# tree = ET.ElementTree(root)
# tree.write('output.xml', encoding='utf-8', xml_declaration=True, pretty_print=True)

