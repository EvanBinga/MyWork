



import xml.etree.ElementTree as ET
import datetime
import xml.dom.minidom

# Получение текущей даты и времени по Московскому времени
moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
formatted_time = moscow_time.strftime('%Y-%m-%dT%H:%M:%S+03:00')

# Загрузка исходного XML файла
xml_path = '/Users/evan/Desktop/tov.xml'  # Путь к вашему XML файлу
tree = ET.parse(xml_path)
root = tree.getroot()

categories = [
    {"id": "57", "url": "https://altaircom.ru/product-category/katalog/", "name": "Каталог"},
    {"id": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/", "name": "Вентиляция корпусов"},
    {"id": "1091", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/metallicheskie-vvody-s-ventilyacziej/", "name": "Металлические вводы вентиляцией"},
    {"id": "215", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/metallicheskij-klapan-vyravnivaniya-davleniya/", "name": "Металлический клапан выравнивания давления"},
    {"id": "1105", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/plastikovye-vvody-s-ventilyacziej/", "name": "Пластиковые вводы вентиляцией"},
    {"id": "390", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/plastikovyj-klapan-vyravnivaniya-davleniya/", "name": "Пластиковый клапан выравнивания давления"},
    {"id": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/", "name": "Кабельные вводы"},
    {"id": "1109", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/membrannye-kabelnye-vvody/", "name": "Мембранные кабельные вводы"},
    {"id": "417", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/metallicheskie-kabelnye-vvody/", "name": "Металлические кабельные вводы"},
    {"id": "217", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/plastikovye-kabelnye-vvody/", "name": "Пластиковые кабельные вводы"},
    {"id": "191", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-din-rejku/", "name": "Клеммы Din Рейку"},
    {"id": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-din-rejku/", "name": "Клеммы на печатную плату"},
    {"id": "152", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/barernye-klemmy/", "name": "Барьерные клеммы"},
    {"id": "67", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/vintovye-klemmnye-bloki/", "name": "Винтовые клеммные блоки"},
    {"id": "62", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/klemmy-dlya-smd-montazha/", "name": "Клеммы для SMD монтажа"},
    {"id": "66", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/nazhimnye-bezvintovye-klemmy/", "name": "Нажимные безвинтовые клеммы"},
    {"id": "161", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/promyshlennye-razemy/", "name": "Промышленные разъемы"},
    {"id": "161", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/razemnye-klemmnye-bloki/", "name": "Разъемные клеммные блоки"},
    {"id": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/", "name": "Разъемы питания"},
    {"id": "377", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-kabelnye-sborki/", "name": "Герметичные кабельные сборки"},
    {"id": "326", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-klemmnye-razvetviteli/", "name": "Герметичные клеммные разветвители"},
    {"id": "363", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-razbornye-razemy/", "name": "Герметичные разборные разъемы"},
    {"id": "64", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/linejnye-germetichnye-razemy/", "name": "Линейные герметичные разъемы"},
    {"id": "491", "url": "https://altaircom.ru/product-category/katalog/rele/", "name": "Реле"},
    {"id": "725", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/avtomobilnye-rele/", "name": "Автомобильные реле"},
    {"id": "788", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/germetichnye-rele/", "name": "Герметичные реле"},
    {"id": "561", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/promyshlennye-rele/", "name": "Промышленные реле"},
    {"id": "939", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/rele-s-magnitnoj-blokirovkoj/", "name": "Реле с магнитной блокировкой"},
    {"id": "492", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/signalnye-rele/", "name": "Сигнальные реле"},
    {"id": "493", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/silovye-rele/", "name": "Силовые реле"},
    {"id": "58",  "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/", "name": "Соединительные клеммы"},
    {"id": "183", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/klemmy-s-zashhitoj/", "name": "Клеммы с защитой"},
    {"id": "60", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/nazhimnye-klemmniki/", "name": "Нажимные клеммники"},
    {"id": "65", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/prozrachnye-bystrozazhimnye-klemmy/", "name": "Прозрачные быстрозажимные клеммы"},
    {"id": "169", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/prohodnye-vintovye-klemmy/", "name": "Проходные-винтовые клеммы"},
    {"id": "59", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/rychazhkovye-soedinitelnye-klemmy/", "name": "Рычажковые соединительные клеммы"},
]

# Создание новой структуры данных в формате YML
yml_root = ET.Element('yml_catalog')
yml_root.set('date', formatted_time)

# Элемент categories
categories_elem = ET.SubElement(yml_root, 'categories')
for category_data in categories:
    category = ET.SubElement(categories_elem, 'category')
    category.set('id', category_data["id"])
    if "parentId" in category_data:
        category.set('parentId', category_data["parentId"])
    category.set('url', category_data["url"])
    category.text = category_data["name"]

# Элемент shop
shop = ET.SubElement(yml_root, 'shop')
name = ET.SubElement(shop, 'name')
name.text = 'altair'  # Замените на ваше название магазина
url = ET.SubElement(shop, 'url')
url.text = 'https://altaircom.ru/'  # Замените на ссылку вашего сайта

# Элемент offers
offers = ET.SubElement(shop, 'offers')

for i, post in enumerate(root.findall('.//post')):
    offer = ET.SubElement(offers, 'offer')
    offer.set('id', str(i + 100))
    offer.set('available', 'true')
    offer.set('group_id', f'100-{i + 1}')

    current_category = categories[i % len(categories)]
    category_id_elem = ET.SubElement(offer, 'categoryId')
    category_id_elem.text = current_category["id"]

    title_elem = post.find('Title')
    if title_elem is not None:
        name_elem = ET.SubElement(offer, 'name')
        name_elem.text = title_elem.text

    price_elem = post.find('Price')
    if price_elem is not None:
        price_value = price_elem.text
        price_elem = ET.SubElement(offer, 'price')
        price_elem.text = price_value

    vendor_elem = ET.SubElement(offer, 'vendor')
    vendor_elem.text = 'ortac'

    permalink_elem = post.find('Permalink')
    if permalink_elem is not None:
        url_elem = ET.SubElement(offer, 'url')
        url_elem.text = permalink_elem.text

    sku_elem = post.find('Sku')  # Извлечение значения Sku из исходного XML
    if sku_elem is not None:
        vendor_code_elem = ET.SubElement(offer, 'vendorCode')  # Создание элемента vendorCode
        vendor_code_elem.text = sku_elem.text

        picture_url_elem = post.find('ImageURL')  # Извлечение URL изображения из исходного XML
    if picture_url_elem is not None:
        picture_elem = ET.SubElement(offer, 'picture')  # Создание элемента picture
        picture_elem.text = picture_url_elem.text  


# Создание объекта для форматирования XML
xml_string = ET.tostring(yml_root, encoding='utf-8')
dom = xml.dom.minidom.parseString(xml_string)

# Сохранение новой структуры данных в файл YML с отступами и переносами строк
output_path = '/Users/evan/Desktop/output_feed.xml'
with open(output_path, 'wb') as file:
    file.write(dom.toprettyxml(encoding='utf-8'))

print(f"Файл сохранен как {output_path}")





# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import Element, SubElement
# import datetime
# import xml.dom.minidom

# # Получение текущей даты и времени по Московскому времени
# moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
# formatted_time = moscow_time.strftime('%Y-%m-%dT%H:%M:%S+03:00')

# # Загрузка исходного XML файла
# xml_path = '/Users/evan/Desktop/tov.xml'  # Путь к вашему XML файлу
# tree = ET.parse(xml_path)
# root = tree.getroot()


# # Создание новой структуры данных в формате YML
# yml_root = Element('yml_catalog')
# yml_root.set('date', formatted_time)

# # Создание элемента categories и добавление в корневой элемент yml_root
# categories_elem = SubElement(yml_root, 'categories')

# for category_data in categories:
#     category = SubElement(categories_elem, 'category')
#     category.set('id', category_data["id"])
#     if "parentId" in category_data:
#         category.set('parentId', category_data["parentId"])
#     category.set('url', category_data["url"])
#     category.text = category_data["name"]

# shop = SubElement(yml_root, 'shop')

# # Элемент с названием магазина
# name = SubElement(shop, 'name')
# name.text = 'altair'  # Замените на ваше название магазина

# # Элемент с ссылкой на магазин
# url = SubElement(shop, 'url')
# url.text = 'https://altaircom.ru/'  # Замените на ссылку вашего сайта


# # Проход по записям (постам) исходного XML и создание "offer" элементов в новой структуре YML
# offers = SubElement(shop, 'offers')
# offers = SubElement(shop, 'offers')

# # ...

# # ...

# for i, post in enumerate(root.findall('.//post')):
#     offer = SubElement(offers, 'offer')
#     offer.set('id', str(i + 100))  # Установка атрибута id с учетом смещения на 100
    
#     # ... (остальные атрибуты)

#     # Извлечение значения Title из исходного XML
#     title_elem = post.find('Title')
#     if title_elem is not None:
#         name_elem = SubElement(offer, 'name')
#         name_elem.text = title_elem.text
    
#     # Извлечение значения Price из исходного XML
#     price_elem = post.find('Price')
#     if price_elem is not None:
#         price_value = price_elem.text
#         price_elem = SubElement(offer, 'price')
#         price_elem.text = price_value
    
#     # Пример добавления производителя (vendor) для каждого товара
#     vendor_elem = SubElement(offer, 'vendor')
#     vendor_elem.text = 'ortac'  # Замените на желаемое значение производителя
    
#     # Извлечение значения Permalink из исходного XML и добавление в элемент <url> в YML
#     permalink_elem = post.find('Permalink')
#     if permalink_elem is not None:
#         url_elem = SubElement(offer, 'url')
#         url_elem.text = permalink_elem.text

# # ...

# # ...


# for i, post in enumerate(root.findall('.//post')):
#     offer = SubElement(offers, 'offer')
#     offer.set('id', str(i + 100))  # Установка атрибута id с учетом смещения на 100
    
#     # Добавление других атрибутов, например, available и group_id
#     offer.set('available', 'true')
#     offer.set('group_id', f'100-{i + 1}')
    
#     # Получение текущей категории из массива категорий
#     current_category = categories[i % len(categories)]
    
#     # Создание элемента categoryId и добавление в offer
#     category_id_elem = SubElement(offer, 'categoryId')
#     category_id_elem.text = current_category["id"]
    
#     # Извлечение значения Title из исходного XML
#     title_elem = post.find('Title')
#     if title_elem is not None:
#         name_elem = SubElement(offer, 'name')
#         name_elem.text = title_elem.text
    
#     # Извлечение значения Price из исходного XML
#     price_elem = post.find('Price')
#     if price_elem is not None:
#         price_value = price_elem.text
#         price_elem = SubElement(offer, 'price')
#         price_elem.text = price_value
    
#     # Пример добавления производителя (vendor) для каждого товара
#     vendor_elem = SubElement(offer, 'vendor')
#     vendor_elem.text = 'ortac'  # Замените на желаемое значение производителя

# # ...

# # Создание объекта для форматирования XML
# xml_string = ET.tostring(yml_root, encoding='utf-8')
# dom = xml.dom.minidom.parseString(xml_string)

# # Сохранение новой структуры данных в файл YML с отступами и переносами строк
# output_path = '/Users/evan/Desktop/output_feed.yml'
# with open(output_path, 'wb') as file:
#     file.write(dom.toprettyxml(encoding='utf-8'))


# for post in root.findall('.//post'):
#     content_elem = post.find('Content')
#     if content_elem is not None:
#         cdata_section = content_elem.text
#         # Здесь вы можете обработать содержимое cdata_section и заменить его
#         # Например, используя replace() или регулярные выражения
#         # Новое значение для замены
#         new_content = cdata_section.replace('старое значение', 'новое значение')
#         # Присвоить новое значение cdata_section
#         content_elem.text = new_content


Обезбо найз либо нимисил либо китонал противоспол
вместе с ними 3 раза в день любые из них 
 амепразол 1 раз утром и 1 раз вечером 
нексиум принимается 1 раз в день для защиты желутка 

оплекатор кузнецова лежать с 5 до 40 минут 
пожосчте диван 
головй спиной ложишься в идеале каждый день перед сном 
местно на спину намазть где крестец и попа можно мазать бальзамимами мазами 911 а называется сабельник или окопник 2 раза в день утрром и вечером 

невзоролог 


# print(f"Файл сохранен как {output_path}")



# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import Element, SubElement
# import datetime
# import xml.dom.minidom

# # Получение текущей даты и времени по Московскому времени
# moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
# formatted_time = moscow_time.strftime('%Y-%m-%dT%H:%M:%S+03:00')

# # Загрузка исходного XML файла
# xml_path = '/Users/evan/Desktop/tovtest.xml'  # Путь к вашему XML файлу
# tree = ET.parse(xml_path)
# root = tree.getroot()

# # Пример массива категорий, можно оставить пустым и заполнять динамически
# categories = [
#     {"id": "57", "url": "https://altaircom.ru/product-category/katalog/", "name": "Каталог"},
#     {"id": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/", "name": "Вентиляция корпусов"},
#     {"id": "1091", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/metallicheskie-vvody-s-ventilyacziej/", "name": "Металлические вводы вентиляцией"},
#     {"id": "215", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/metallicheskij-klapan-vyravnivaniya-davleniya/", "name": "Металлический клапан выравнивания давления"},
#     {"id": "1105", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/plastikovye-vvody-s-ventilyacziej/", "name": "Пластиковые вводы вентиляцией"},
#     {"id": "390", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/plastikovyj-klapan-vyravnivaniya-davleniya/", "name": "Пластиковый клапан выравнивания давления"},
#     {"id": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/", "name": "Кабельные вводы"},
#     {"id": "1109", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/membrannye-kabelnye-vvody/", "name": "Мембранные кабельные вводы"},
#     {"id": "417", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/metallicheskie-kabelnye-vvody/", "name": "Металлические кабельные вводы"},
#     {"id": "217", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/plastikovye-kabelnye-vvody/", "name": "Пластиковые кабельные вводы"},
#     {"id": "191", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-din-rejku/", "name": "Клеммы Din Рейку"},
#     {"id": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-din-rejku/", "name": "Клеммы на печатную плату"},
#     {"id": "152", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/barernye-klemmy/", "name": "Барьерные клеммы"},
#     {"id": "67", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/vintovye-klemmnye-bloki/", "name": "Винтовые клеммные блоки"},
#     {"id": "62", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/klemmy-dlya-smd-montazha/", "name": "Клеммы для SMD монтажа"},
#     {"id": "66", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/nazhimnye-bezvintovye-klemmy/", "name": "Нажимные безвинтовые клеммы"},
#     {"id": "161", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/promyshlennye-razemy/", "name": "Промышленные разъемы"},
#     {"id": "161", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/razemnye-klemmnye-bloki/", "name": "Разъемные клеммные блоки"},
#     {"id": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/", "name": "Разъемы питания"},
#     {"id": "377", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-kabelnye-sborki/", "name": "Герметичные кабельные сборки"},
#     {"id": "326", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-klemmnye-razvetviteli/", "name": "Герметичные клеммные разветвители"},
#     {"id": "363", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-razbornye-razemy/", "name": "Герметичные разборные разъемы"},
#     {"id": "64", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/linejnye-germetichnye-razemy/", "name": "Линейные герметичные разъемы"},
#     {"id": "491", "url": "https://altaircom.ru/product-category/katalog/rele/", "name": "Реле"},
#     {"id": "725", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/avtomobilnye-rele/", "name": "Автомобильные реле"},
#     {"id": "788", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/germetichnye-rele/", "name": "Герметичные реле"},
#     {"id": "561", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/promyshlennye-rele/", "name": "Промышленные реле"},
#     {"id": "939", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/rele-s-magnitnoj-blokirovkoj/", "name": "Реле с магнитной блокировкой"},
#     {"id": "492", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/signalnye-rele/", "name": "Сигнальные реле"},
#     {"id": "493", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/silovye-rele/", "name": "Силовые реле"},
#     {"id": "58",  "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/", "name": "Соединительные клеммы"},
#     {"id": "183", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/klemmy-s-zashhitoj/", "name": "Клеммы с защитой"},
#     {"id": "60", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/nazhimnye-klemmniki/", "name": "Нажимные клеммники"},
#     {"id": "65", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/prozrachnye-bystrozazhimnye-klemmy/", "name": "Прозрачные быстрозажимные клеммы"},
#     {"id": "169", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/prohodnye-vintovye-klemmy/", "name": "Проходные-винтовые клеммы"},
#     {"id": "59", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/rychazhkovye-soedinitelnye-klemmy/", "name": "Рычажковые соединительные клеммы"},
# ]


# # Создание новой структуры данных в формате YML
# yml_root = Element('yml_catalog')
# yml_root.set('date', formatted_time)

# # Создание элемента categories и добавление в корневой элемент yml_root
# categories_elem = SubElement(yml_root, 'categories')

# for category_data in categories:
#     category = SubElement(categories_elem, 'category')
#     category.set('id', category_data["id"])
#     if "parentId" in category_data:
#         category.set('parentId', category_data["parentId"])
#     category.set('url', category_data["url"])
#     category.text = category_data["name"]

# shop = SubElement(yml_root, 'shop')

# # Элемент с названием магазина
# name = SubElement(shop, 'name')
# name.text = 'altair'  # Замените на ваше название магазина

# # Элемент с ссылкой на магазин
# url = SubElement(shop, 'url')
# url.text = 'https://altaircom.ru/'  # Замените на ссылку вашего сайта


# # Проход по записям (постам) исходного XML и создание "offer" элементов в новой структуре YML
# offers = SubElement(shop, 'offers')

# for i, post in enumerate(root.findall('.//post')):
#     offer = SubElement(offers, 'offer')
#     offer.set('id', str(i + 100))  # Установка атрибута id с учетом смещения на 100
    
#     # Добавление других атрибутов, например, available и group_id
#     offer.set('available', 'true')
#     offer.set('group_id', f'100-{i + 1}')
    
#     # Получение текущей категории из массива категорий
#     current_category = categories[i % len(categories)]
    
#     # Создание элемента categoryId и добавление в offer
#     category_id_elem = SubElement(offer, 'categoryId')
#     category_id_elem.text = current_category["id"]
    
#     # Здесь создайте и заполните остальные элементы в "offer" в соответствии с вашим форматом YML
#     # Например, <name>, <url>, <price>, и так далее
    
#     # Пример создания и заполнения элемента "name"
#     name_elem = SubElement(offer, 'name')
#     title = post.find('Title').text
#     name_elem.text = title

# # Создание объекта для форматирования XML
# xml_string = ET.tostring(yml_root, encoding='utf-8')
# dom = xml.dom.minidom.parseString(xml_string)

# # Сохранение новой структуры данных в файл YML с отступами и переносами строк
# output_path = '/Users/evan/Desktop/output_feed.yml'
# with open(output_path, 'wb') as file:
#     file.write(dom.toprettyxml(encoding='utf-8'))

# print(f"Файл сохранен как {output_path}")









# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import Element, SubElement
# import datetime
# import xml.dom.minidom

# # Получение текущей даты и времени по Московскому времени
# moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
# formatted_time = moscow_time.strftime('%Y-%m-%dT%H:%M:%S+03:00')

# # Загрузка исходного XML файла
# xml_path = '/Users/evan/Desktop/tovtest.xml'  # Путь к вашему XML файлу
# tree = ET.parse(xml_path)
# root = tree.getroot()




# # Создание новой структуры данных в формате YML
# yml_root = Element('yml_catalog')
# yml_root.set('date', formatted_time)

# shop = SubElement(yml_root, 'shop')




# categories = [
#     {"id": "57", "url": "https://altaircom.ru/product-category/katalog/", "name": "Каталог"},
#     {"id": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/", "name": "Вентиляция корпусов"},
#     {"id": "1091", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/metallicheskie-vvody-s-ventilyacziej/", "name": "Металлические вводы вентиляцией"},
#     {"id": "215", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/metallicheskij-klapan-vyravnivaniya-davleniya/", "name": "Металлический клапан выравнивания давления"},
#     {"id": "1105", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/plastikovye-vvody-s-ventilyacziej/", "name": "Пластиковые вводы вентиляцией"},
#     {"id": "390", "parentId": "214", "url": "https://altaircom.ru/product-category/katalog/ventilyacziya-vlagozashhishhennyh-korpusov/plastikovyj-klapan-vyravnivaniya-davleniya/", "name": "Пластиковый клапан выравнивания давления"},
#     {"id": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/", "name": "Кабельные вводы"},
#     {"id": "1109", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/membrannye-kabelnye-vvody/", "name": "Мембранные кабельные вводы"},
#     {"id": "417", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/metallicheskie-kabelnye-vvody/", "name": "Металлические кабельные вводы"},
#     {"id": "217", "parentId": "216", "url": "https://altaircom.ru/product-category/katalog/kabelnye-vvody/plastikovye-kabelnye-vvody/", "name": "Пластиковые кабельные вводы"},
#     {"id": "191", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-din-rejku/", "name": "Клеммы Din Рейку"},
#     {"id": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-din-rejku/", "name": "Клеммы на печатную плату"},
#     {"id": "152", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/barernye-klemmy/", "name": "Барьерные клеммы"},
#     {"id": "67", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/vintovye-klemmnye-bloki/", "name": "Винтовые клеммные блоки"},
#     {"id": "62", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/klemmy-dlya-smd-montazha/", "name": "Клеммы для SMD монтажа"},
#     {"id": "66", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/nazhimnye-bezvintovye-klemmy/", "name": "Нажимные безвинтовые клеммы"},
#     {"id": "161", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/promyshlennye-razemy/", "name": "Промышленные разъемы"},
#     {"id": "161", "parentId": "61", "url": "https://altaircom.ru/product-category/katalog/klemmy-na-pechatnuyu-platu/razemnye-klemmnye-bloki/", "name": "Разъемные клеммные блоки"},
#     {"id": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/", "name": "Разъемы питания"},
#     {"id": "377", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-kabelnye-sborki/", "name": "Герметичные кабельные сборки"},
#     {"id": "326", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-klemmnye-razvetviteli/", "name": "Герметичные клеммные разветвители"},
#     {"id": "363", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/germetichnye-razbornye-razemy/", "name": "Герметичные разборные разъемы"},
#     {"id": "64", "parentId": "63", "url": "https://altaircom.ru/product-category/katalog/razemy-pitaniya/linejnye-germetichnye-razemy/", "name": "Линейные герметичные разъемы"},
#     {"id": "491", "url": "https://altaircom.ru/product-category/katalog/rele/", "name": "Реле"},
#     {"id": "725", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/avtomobilnye-rele/", "name": "Автомобильные реле"},
#     {"id": "788", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/germetichnye-rele/", "name": "Герметичные реле"},
#     {"id": "561", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/promyshlennye-rele/", "name": "Промышленные реле"},
#     {"id": "939", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/rele-s-magnitnoj-blokirovkoj/", "name": "Реле с магнитной блокировкой"},
#     {"id": "492", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/signalnye-rele/", "name": "Сигнальные реле"},
#     {"id": "493", "parentId": "491", "url": "https://altaircom.ru/product-category/katalog/rele/silovye-rele/", "name": "Силовые реле"},
#     {"id": "58",  "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/", "name": "Соединительные клеммы"},
#     {"id": "183", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/klemmy-s-zashhitoj/", "name": "Клеммы с защитой"},
#     {"id": "60", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/nazhimnye-klemmniki/", "name": "Нажимные клеммники"},
#     {"id": "65", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/prozrachnye-bystrozazhimnye-klemmy/", "name": "Прозрачные быстрозажимные клеммы"},
#     {"id": "169", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/prohodnye-vintovye-klemmy/", "name": "Проходные-винтовые клеммы"},
#     {"id": "59", "parentId": "58", "url": "https://altaircom.ru/product-category/katalog/soedinitelnye-klemmy/rychazhkovye-soedinitelnye-klemmy/", "name": "Рычажковые соединительные клеммы"},
# ]
