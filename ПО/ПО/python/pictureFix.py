import xml.etree.ElementTree as ET

# Открываем исходные XML-файлы
with open('ttttt.xml', 'r', encoding='utf-8') as source_file:
    source_content = source_file.read()

with open('modified_feed_yml.xml', 'r', encoding='utf-8') as compare_file:
    compare_content = compare_file.read()

# Создаем словарь для хранения соответствий SKU и ID
sku_to_id = {}

# Парсим исходный файл и извлекаем SKU и ID
source_root = ET.fromstring(source_content)
for post in source_root.findall('.//post'):
    sku = post.find('SKU').text
    id = post.find('id').text
    sku_to_id[sku] = id

# Создаем новый XML-файл с обновленными ID
compare_root = ET.fromstring(compare_content)
for offer in compare_root.findall('.//offer'):
    vendor_code = offer.find('vendorCode').text
    if vendor_code in sku_to_id:
        id = sku_to_id[vendor_code]
        offer.set('id', id)

# Сохраняем новый XML-файл
new_xml_content = ET.tostring(compare_root, encoding='utf-8').decode()
with open('feeeeed.xml', 'w', encoding='utf-8') as new_file:
    new_file.write(new_xml_content)
























# import re

# # Открываем текстовый файл и считываем его содержимое
# with open('tovary.xml', 'r', encoding='utf-8') as file:
#     text_content = file.read()

# # Используем регулярные выражения для извлечения информации
# id_values = re.findall(r'<id>(\d+)</id>', text_content)
# title_values = re.findall(r'<Title>(.*?)</Title>', text_content)
# sku_values = re.findall(r'<SKU>(\d+)</SKU>', text_content)

# # Создаем новый XML-файл и записываем в него извлеченную информацию
# with open('ttttt.xml', 'w', encoding='utf-8') as new_file:
#     new_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
#     new_file.write('<root>\n')
#     for id, title, sku in zip(id_values, title_values, sku_values):
#         new_file.write(f'\t<post>\n')
#         new_file.write(f'\t\t<id>{id}</id>\n')
#         new_file.write(f'\t\t<Title><![CDATA[{title}]]></Title>\n')
#         new_file.write(f'\t\t<SKU>{sku}</SKU>\n')
#         new_file.write(f'\t</post>\n')
#     new_file.write('</root>\n')



















# import xml.etree.ElementTree as ET

# # Открываем XML-файл
# tree = ET.parse('tovary.xml')
# root = tree.getroot()

# # Проходим по всем элементам post в вашем XML
# for post in root.findall('.//post'):
#     sku = post.find('SKU').text  # Получаем значение SKU из XML

#     # Теперь найдем соответствующий товар в фиде и добавим айдишник
#     for offer in root.findall('.//offer'):
#         vendorCode = offer.find('vendorCode').text  # Получаем значение vendorCode из фида

#         # Сравниваем SKU и vendorCode, если они совпадают, добавляем айдишник в атрибут id
#         if sku == vendorCode:
#             offer.set('id', post.find('id').text)

# # Сохраняем измененный фид обратно в файл
# tree.write('modified_feed_yml.xml')






# import re
# import xml.etree.ElementTree as ET

# # Открываем XML-файл
# tree = ET.parse('tovary.xml')
# root = tree.getroot()

# # Функция для удаления ненужных символов из текста CDATA
# def clean_cdata(text):
#     return re.sub(r'[<>]', '', text)

# # Проходим по всем элементам post в вашем XML
# for post in root.findall('.//post'):
#     # Получаем текст из CDATA блоков и очищаем его
#     title = clean_cdata(post.find('Title').text)
#     content = clean_cdata(post.find('Content').text)

#     # Устанавливаем очищенный текст обратно в элементы XML
#     post.find('Title').text = '<![CDATA[' + title + ']]>'
#     post.find('Content').text = '<![CDATA[' + content + ']]>'

# # Сохраняем обновленный XML обратно в файл
# tree.write('tovv.xml')





































# import xml.etree.ElementTree as ET
# import os

# # Получите путь к файлу на рабочем столе с данными
# desktop_path = os.path.expanduser("~/Desktop")  # Путь к рабочему столу на macOS, для других ОС может потребоваться другой путь

# # Укажите имя вашего XML-файла с данными
# data_xml_file_name = "tovary.xml"

# # Создайте полный путь к файлу
# data_xml_file_path = os.path.join(desktop_path, data_xml_file_name)

# # Откройте файл и считайте его содержимое
# with open(data_xml_file_path, "r", encoding="utf-8") as data_file:
#     data_xml_string = data_file.read()

# # Создайте объект ElementTree для данных
# data_tree = ET.ElementTree(ET.fromstring(data_xml_string))

# # Получите корневой элемент данных
# data_root = data_tree.getroot()

# # Создайте структуру данных для хранения соответствий атрибутов id и SKU
# id_sku_mapping = {}

# # Пройдите по данным и сохраните соответствия id и SKU
# for post in data_root.findall(".//post"):
#     id_element = post.find("id")
#     sku_element = post.find("SKU")
#     if id_element is not None and sku_element is not None:
#         id_value = id_element.text
#         sku_value = sku_element.text
#         if id_value and sku_value:
#             id_sku_mapping[sku_value] = id_value

# # Получите путь к целевому XML-файлу (фиду)
# target_xml_file_name = "modified_feed_yml.xml"
# target_xml_file_path = os.path.join(desktop_path, target_xml_file_name)

# # Откройте целевой XML-файл и считайте его содержимое
# with open(target_xml_file_path, "r", encoding="utf-8") as target_file:
#     target_xml_string = target_file.read()

# # Создайте объект ElementTree для целевого XML-файла (фида)
# target_tree = ET.ElementTree(ET.fromstring(target_xml_string))

# # Получите корневой элемент целевого XML-файла (фида)
# target_root = target_tree.getroot()

# # Пройдите по каждому элементу <offer> в целевом XML-файле (фиде)
# for offer in target_root.findall(".//offer"):
#     # Найдите SKU в элементе <vendorCode>
#     sku_element = offer.find("vendorCode")
#     if sku_element is not None and sku_element.text:
#         sku_value = sku_element.text.strip()
#         # Если есть соответствие SKU в структуре данных, добавьте его значение id в атрибут id элемента <offer>
#         if sku_value in id_sku_mapping:
#             offer.set("id", id_sku_mapping[sku_value])

# # Преобразуйте объект ElementTree обратно в строку
# new_target_xml_string = ET.tostring(target_root, encoding="unicode")

# # Теперь new_target_xml_string содержит обновленный XML-файл (фид) с добавленными атрибутами id

# # Можете сохранить новый XML-файл, если необходимо
# new_target_xml_file_path = os.path.join(desktop_path, "updated_feed_yml.xml")
# with open(new_target_xml_file_path, "w", encoding="utf-8") as new_target_file:
#     new_target_file.write(new_target_xml_string)
