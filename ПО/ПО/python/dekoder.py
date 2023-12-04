import csv
import xml.etree.ElementTree as ET

csv_file_path = '/Users/evan/Desktop/product.csv'  # Замените на путь к вашему CSV файлу
xml_file_path = '/Users/evan/Desktop/output.xml'  # Путь для сохранения XML файла

# Создание корневого элемента XML
root = ET.Element('data')

# Чтение CSV файла и добавление данных в XML
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        post_elem = ET.SubElement(root, 'post')
        post_elem.text = '\n    '  # Добавляем отступ и перенос строки перед <post>

        for column_name, value in row.items():
            if value is not None:
                column_elem = ET.SubElement(post_elem, column_name)
                clean_value = value.strip()  # Удаление начальных и конечных пробелов и символов новой строки
                column_elem.text = clean_value
                column_elem.tail = '\n      '  # Добавляем отступ и перенос строки после элемента

# Создание объекта ElementTree
tree = ET.ElementTree(root)

# Сохранение XML в файл с отступами и читаемой разметкой
tree.write(xml_file_path, encoding='utf-8', xml_declaration=True, method="xml")

print(f"Файл сохранен как {xml_file_path}")

# import csv
# import xml.etree.ElementTree as ET

# csv_file_path = '/Users/evan/Desktop/product.csv'  # Замените на путь к вашему CSV файлу
# xml_file_path = '/Users/evan/Desktop/output.xml'  # Путь для сохранения XML файла

# # Создание корневого элемента XML
# root = ET.Element('data')

# # Чтение CSV файла и добавление данных в XML
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         post_elem = ET.SubElement(root, 'post')
#         post_elem.text = '\n    '  # Добавляем отступ и перенос строки перед <post>

#         for column_name, value in row.items():
#             if value is not None:
#                 column_elem = ET.SubElement(post_elem, column_name)
#                 column_elem.text = value
#                 column_elem.tail = '\n      '  # Добавляем отступ и перенос строки после элемента

# # Создание объекта ElementTree
# tree = ET.ElementTree(root)

# # Сохранение XML в файл с отступами и читаемой разметкой
# tree.write(xml_file_path, encoding='utf-8', xml_declaration=True, method="xml")

# print(f"Файл сохранен как {xml_file_path}")



# import csv
# import xml.etree.ElementTree as ET
# import xml.dom.minidom

# csv_file_path = '/Users/evan/Desktop/product.csv'  # Замените на путь к вашему CSV файлу
# xml_file_path = '/Users/evan/Desktop/output.xml'  # Путь для сохранения XML файла

# # Создание корневого элемента XML
# root = ET.Element('data')

# # Чтение CSV файла и добавление данных в XML
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         post_elem = ET.SubElement(root, 'post')

#         for column_name, value in row.items():
#             if value is not None:
#                 # Оборачиваем значения в CDATA, если это необходимо
#                 if column_name in ['Content']:
#                     column_elem = ET.SubElement(post_elem, column_name)
#                     cdata = ET.CDATA(value)
#                     column_elem.append(cdata)
#                 else:
#                     column_elem = ET.SubElement(post_elem, column_name)
#                     column_elem.text = value

# # Создание объекта для форматирования XML
# xml_string = ET.tostring(root, encoding='utf-8').decode('utf-8')

# # Сохранение XML в файл
# with open(xml_file_path, 'w', encoding='utf-8') as xml_file:
#     xml_file.write(xml_string)



# import csv
# import xml.etree.ElementTree as ET
# import xml.dom.minidom

# csv_file_path = '/Users/evan/Desktop/product.csv'  # Замените на путь к вашему CSV файлу
# xml_file_path = '/Users/evan/Desktop/output.xml'  # Путь для сохранения XML файла

# # Создание корневого элемента XML
# root = ET.Element('data')

# # Чтение CSV файла и добавление данных в XML
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         post_elem = ET.SubElement(root, 'post')

#         for column_name, value in row.items():
#             if value is not None:
#                 column_elem = ET.SubElement(post_elem, column_name)
#                 column_elem.text = value

# # Создание объекта для форматирования XML
# xml_string = ET.tostring(root, encoding='utf-8').decode('utf-8')

# # Сохранение XML в файл
# with open(xml_file_path, 'w', encoding='utf-8') as xml_file:
#     xml_file.write(xml_string)
