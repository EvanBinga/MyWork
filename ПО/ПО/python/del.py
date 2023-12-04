import xml.etree.ElementTree as ET

# Загрузите ваш XML-файл
tree = ET.parse("tovary.xml")
root = tree.getroot()

# Пройдитесь по всем элементам <post>
for post in root.findall(".//post"):
    # Найдите элемент Content
    content = post.find("Content")
    if content is not None:
        # Удалите CDATA из элемента Content
        for cdata in content.findall(".//"):
            if cdata.text is not None and "<![CDATA[" in cdata.text:
                cdata.text = None

# Сохраните обновленный XML-файл
tree.write("updated_file.xml")
