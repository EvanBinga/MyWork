import csv
import xml.etree.ElementTree as ET

# Путь к вашему фиду XML
feed_xml_path = '/Users/evan/Desktop/output_feed.xml'

# Путь к вашему CSV файлу
csv_file_path = '/Users/evan/Desktop/product.csv'

# Загрузка CSV файла в словарь, где ключ - Имя, значение - список атрибутов и значений
name_to_attributes_values = {}
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        attributes_values = []
        for i in range(1, 12):  # Проходим по столбцам Значение атрибутов 1 до Значение атрибутов 11
            attribute_name_key = f'Название атрибута {i}'
            value_key = f'Значения атрибутов {i}'
            attribute_name = row.get(attribute_name_key)
            attribute_value = row.get(value_key)
            if attribute_name is not None and attribute_value is not None:
                attribute_name = attribute_name.strip()
                attribute_value = attribute_value.strip()
                if attribute_name and attribute_value:
                    attributes_values.append((attribute_name, attribute_value))
        name_to_attributes_values[row['Имя']] = attributes_values

# Загрузка фида XML
tree = ET.parse(feed_xml_path)
root = tree.getroot()

# Проходимся по каждому оферу и добавляем теги <param> с атрибутами и значениями
for offer in root.findall('.//offer'):
    name_elem = offer.find('name')
    if name_elem is not None:
        product_name = name_elem.text
        if product_name in name_to_attributes_values:
            attributes_values = name_to_attributes_values[product_name]
            new_params = []  # Создаем список для новых тегов <param>
            for attribute_name, attribute_value in attributes_values:
                existing_param = offer.find(f"./param[@name='{attribute_name}']")
                if existing_param is not None:
                    existing_param.text = attribute_value
                else:
                    param_elem = ET.Element('param', name=attribute_name)  # Создаем новый тег <param>
                    param_elem.text = attribute_value
                    new_params.append(param_elem)  # Добавляем его в список
            for existing_param in offer.findall('param'):
                offer.remove(existing_param)  # Удаляем существующие теги <param>
            for new_param in new_params:
                offer.append(new_param)  # Добавляем новые теги <param> к элементу <offer>

# Сохранение обновленного фида XML
tree.write(feed_xml_path, encoding='utf-8', xml_declaration=True, method="xml")
print(f"Обновленный фид сохранен как {feed_xml_path}")


# import csv
# import xml.etree.ElementTree as ET

# # Путь к вашему фиду XML
# feed_xml_path = '/Users/evan/Desktop/output_feed.yml'

# # Путь к вашему CSV файлу
# csv_file_path = '/Users/evan/Desktop/product.csv'

# # Загрузка CSV файла в словарь, где ключ - Имя, значение - список атрибутов и значений
# name_to_attributes_values = {}
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         attributes_values = []
#         for i in range(1, 12):  # Проходим по столбцам Значение атрибутов 1 до Значение атрибутов 11
#             attribute_name_key = f'Название атрибута {i}'
#             value_key = f'Значения атрибутов {i}'
#             attribute_name = row.get(attribute_name_key)
#             attribute_value = row.get(value_key)
#             if attribute_name is not None and attribute_value is not None:
#                 attribute_name = attribute_name.strip()
#                 attribute_value = attribute_value.strip()
#                 if attribute_name and attribute_value:
#                     attributes_values.append((attribute_name, attribute_value))
#         name_to_attributes_values[row['Имя']] = attributes_values

# # Загрузка фида XML
# tree = ET.parse(feed_xml_path)
# root = tree.getroot()

# # Проходимся по каждому оферу и добавляем тег <param> с атрибутами и значением
# for offer in root.findall('.//offer'):
#     name_elem = offer.find('name')
#     if name_elem is not None:
#         product_name = name_elem.text
#         if product_name in name_to_attributes_values:
#             attributes_values = name_to_attributes_values[product_name]
#             for attribute_name, attribute_value in attributes_values:
#                 existing_param = offer.find(f"./param[@name='{attribute_name}']")
#                 if existing_param is not None:
#                     existing_param.text = attribute_value
#                 else:
#                     param_elem = ET.SubElement(offer, 'param', name=attribute_name)
#                     param_elem.text = attribute_value

# # Сохранение обновленного фида XML
# tree.write(feed_xml_path, encoding='utf-8', xml_declaration=True)
# print(f"Обновленный фид сохранен как {feed_xml_path}")


# import csv
# import xml.etree.ElementTree as ET

# # Путь к вашему фиду XML
# feed_xml_path = '/Users/evan/Desktop/output_feed.yml'

# # Путь к вашему CSV файлу
# csv_file_path = '/Users/evan/Desktop/product.csv'

# # Загрузка CSV файла в словарь, где ключ - Имя, значение - Название атрибута и Значение атрибута
# name_to_attribute_value = {}
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         name_to_attribute_value[row['Имя']] = (row['Название атрибута 1'], row['Значения атрибутов 1'])  # Здесь указаны соответствующие колонки

# # Загрузка фида XML
# tree = ET.parse(feed_xml_path)
# root = tree.getroot()

# # Проходимся по каждому оферу и добавляем тег <param> с атрибутами и значением
# for offer in root.findall('.//offer'):
#     name_elem = offer.find('name')
#     if name_elem is not None:
#         product_name = name_elem.text
#         if product_name in name_to_attribute_value:
#             attribute_name, attribute_value = name_to_attribute_value[product_name]
#             param_elem = ET.SubElement(offer, 'param', name=attribute_name)
#             param_elem.text = attribute_value

# # Сохранение обновленного фида XML
# tree.write(feed_xml_path, encoding='utf-8', xml_declaration=True)
# print(f"Обновленный фид сохранен как {feed_xml_path}")



# import csv
# import xml.etree.ElementTree as ET

# # Путь к вашему фиду XML
# feed_xml_path = '/Users/evan/Desktop/output_feed.yml'

# # Путь к вашему CSV файлу
# csv_file_path = '/Users/evan/Desktop/product.csv'

# # Загрузка CSV файла в словарь, где ключ - Имя, значение - Название атрибута
# name_to_attribute = {}
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         name_to_attribute[row['Имя']] = row['Название атрибута 1']

# # Загрузка фида XML
# tree = ET.parse(feed_xml_path)
# root = tree.getroot()

# # Проходимся по каждому оферу и добавляем тег <param> с атрибутами
# for offer in root.findall('.//offer'):
#     name_elem = offer.find('name')
#     if name_elem is not None:
#         product_name = name_elem.text
#         if product_name in name_to_attribute:
#             attribute_name = name_to_attribute[product_name]
#             attribute_value = name_to_attribute[product_name]
#             param_elem = ET.SubElement(offer, 'param', name=attribute_name)
#             param_elem.text = attribute_value

# # Сохранение обновленного фида XML
# tree.write(feed_xml_path, encoding='utf-8', xml_declaration=True)
# print(f"Обновленный фид сохранен как {feed_xml_path}")





# import csv
# import xml.etree.ElementTree as ET

# # Путь к вашему фиду XML
# feed_xml_path = '/Users/evan/Desktop/output_feed.yml'

# # Путь к вашему CSV файлу
# csv_file_path = '/Users/evan/Desktop/product.csv'

# # Загрузка CSV файла в словарь, где ключ - Имя, значение - название атрибута и значение атрибута
# name_to_attributes = {}
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         name = row['Имя']
#         attribute_name = row['Название атрибута 1']
#         # attribute_value = row['Значение атрибута 1']
#         name_to_attributes[name] = (attribute_name, attribute_value)

# # Загрузка фида XML
# tree = ET.parse(feed_xml_path)
# root = tree.getroot()

# # Проходимся по каждому оферу и добавляем тег <param> с атрибутами и значениями
# for offer in root.findall('.//offer'):
#     name_elem = offer.find('name')
#     if name_elem is not None:
#         product_name = name_elem.text
#         if product_name in name_to_attributes:
#             attribute_name, attribute_value = name_to_attributes[product_name]
#             param_elem = ET.SubElement(offer, 'param', name=attribute_name)
#             param_elem.text = attribute_value

# # Сохранение обновленного фида XML
# tree.write(feed_xml_path, encoding='utf-8', xml_declaration=True)
# print(f"Обновленный фид сохранен как {feed_xml_path}")


# import csv
# import xml.etree.ElementTree as ET

# # Путь к вашему фиду XML
# feed_xml_path = '/Users/evan/Desktop/output_feed.yml'

# # Путь к вашему CSV файлу
# csv_file_path = '/Users/evan/Desktop/product.csv'

# # Загрузка CSV файла в словарь, где ключ - Имя, значение - Название атрибута
# name_to_attribute = {}
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         name_to_attribute[row['Имя']] = row['Название атрибута 1']

# # Загрузка фида XML
# tree = ET.parse(feed_xml_path)
# root = tree.getroot()

# # Проходимся по каждому оферу и добавляем тег <param> с атрибутами
# for offer in root.findall('.//offer'):
#     name_elem = offer.find('name')
#     if name_elem is not None:
#         product_name = name_elem.text
#         if product_name in name_to_attribute:
#             param_elem = ET.SubElement(offer, 'param', name=name_to_attribute[product_name])
#             param_elem.text = name_elem.text

# # Сохранение обновленного фида XML
# tree.write(feed_xml_path, encoding='utf-8', xml_declaration=True)
# print(f"Обновленный фид сохранен как {feed_xml_path}")



# import csv
# import xml.etree.ElementTree as ET

# # Путь к вашему фиду XML
# feed_xml_path = '/Users/evan/Desktop/output_feed.yml'

# # Путь к вашему CSV файлу
# csv_file_path = '/Users/evan/Desktop/product.csv'

# # Загрузка CSV файла в словарь, где ключ - Имя, значение - Название атрибута
# name_to_attribute = {}
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         name_to_attribute[row['Имя']] = row['Название атрибута 1']

# # Загрузка фида XML
# tree = ET.parse(feed_xml_path)
# root = tree.getroot()

# # Проходимся по каждому оферу и добавляем тег <param> с атрибутами
# for offer in root.findall('.//offer'):
#     name_elem = offer.find('name')
#     if name_elem is not None:
#         product_name = name_elem.text
#         if product_name in name_to_attribute:
#             param_elem = ET.SubElement(offer, 'param', name=name_to_attribute[product_name])
#             param_elem.text = name_elem.text

# # Сохранение обновленного фида XML
# updated_feed_path = '/Users/evan/Desktop/updated_feed.xml'
# tree.write(updated_feed_path, encoding='utf-8', xml_declaration=True)
# print(f"Обновленный фид сохранен как {updated_feed_path}")




# import xml.etree.ElementTree as ET
# import csv

# # Путь к вашему фиду XML
# feed_xml_path = '/Users/evan/Desktop/output_feed.yml'

# # Путь к вашему CSV файлу
# csv_file_path = '/Users/evan/Desktop/product.csv'

# # Загрузка фида XML
# tree = ET.parse(feed_xml_path)
# root = tree.getroot()

# # Открываем CSV файл и проходимся по каждой строке
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    
#     for row in csv_reader:
#         product_name = row['Имя']
        
#         # Проходимся по каждому оферу и сравниваем имя с тегом <name>
#         for offer in root.findall('.//offer'):
#             name_elem = offer.find('name')
#             if name_elem is not None and name_elem.text == product_name:
#                 print(f"Найдено совпадение для товара: {product_name}")






# import xml.etree.ElementTree as ET
# import csv

# # Путь к вашему фиду XML
# feed_xml_path = '/Users/evan/Desktop/output_feed.yml'

# # Путь к вашему CSV файлу
# csv_file_path = '/Users/evan/Desktop/product.csv'

# # Загрузка фида XML
# tree = ET.parse(feed_xml_path)
# root = tree.getroot()

# # Открываем CSV файл для чтения
# with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    
#     # Проходимся по каждому оферу
#     for offer in root.findall('.//offer'):
#         # Получаем имя товара
#         name_elem = offer.find('name')
#         if name_elem is not None:
#             product_name = name_elem.text
            
#             # Проходимся по каждой строке CSV и ищем соответствующее значение для товара
#             for row in csv_reader:
#                 attribute_name = row['Название атрибута 1']
#                 attribute_value = row['Значения атрибутов 1']
                
#                 # Если название товара совпадает с ожидаемым значением
#                 if product_name == attribute_name:
#                     param_elem = ET.SubElement(offer, 'param')
#                     param_elem.set('name', attribute_name)
#                     param_elem.text = attribute_value
                    
#                     # Вставляем элемент <param> перед закрывающим тегом </offer>
#                     offer.insert(-1, param_elem)
#                     break  # Прерываем поиск, так как нашли соответствие

# # Сохраняем измененный фид XML
# updated_feed_xml_path = '/Users/evan/Desktop/updated_feed.yml'
# tree.write(updated_feed_xml_path, encoding='utf-8', xml_declaration=True)

# print(f"Фид с добавленными элементами <param> сохранен как {updated_feed_xml_path}")
