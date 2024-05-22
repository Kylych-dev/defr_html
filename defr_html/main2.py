from bs4 import BeautifulSoup

# Пример HTML содержимого
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <p>Stroka-----1--------</p>
    <p>Stroka-----2-------</p>
    <a>Stroka-----3--------</a>
    <p>Stroka-----4--------</p>
    <p>Stroka-----5--------</p>
    <p>Stroka-----6--------</p>
    <p>Stroka-----7--------</p>
    <p>Stroka-----8--------</p>
    <a>Stroka-----9--------</a>
    <p>Stroka-----10--------</p>
    <p>Stroka-----11--------</p>
    <p>Stroka-----12--------</p>
    <p>Stroka-----13--------</p>
    <p>Stroka-----14--------</p>
    <p>Stroka-----15--------</p>
    <p>Stroka-----16--------</p>
    <p>Stroka-----17--------</p>
    <p>Stroka-----18--------</p>
    <p>Stroka-----19--------</p>
    <p>Stroka-----20--------</p>
    <p>Stroka-----21--------</p>
    <p>Stroka-----22--------</p>
    <p>Stroka-----23--------</p>
    <p>Stroka-----24--------</p>
    <p>Stroka-----25--------</p>
    <p>Stroka-----26--------</p>
</body>
</html>
'''


from bs4 import BeautifulSoup, Tag

def insert_delimiters(html_content, max_length=300, delimiter="/*/*/*/*/*/*"):
    soup = BeautifulSoup(html_content, 'html.parser')
    result_html = ""
    current_length = 0

    for element in soup.recursiveChildGenerator():
        if isinstance(element, Tag):
            element_str = str(element)
            if current_length + len(element_str) > max_length:          # Check if adding this element exceeds the max_length
                # Insert delimiter and reset current_length
                result_html += delimiter
                current_length = 0
            # Add the element string to the result and update current_length
            result_html += element_str
            current_length += len(element_str)
        elif element.parent is None:
            # This handles the case for navigable strings that are not wrapped in a tag
            element_str = str(element)
            if current_length + len(element_str) > max_length:
                result_html += delimiter
                current_length = 0
            result_html += element_str
            current_length += len(element_str)

    return result_html



print(insert_delimiters(html_content))










# def split_html(html, max_length):
#     html = BeautifulSoup(html, 'html.parser')
#
#     html_str = str(html)
#
#     if len(html_str) <= max_length:
#         return [html]
#
#     chunks = []
#     current_chunk = BeautifulSoup("", 'html.parser')
#
#     for element in html.descendants:
#         if len(str(current_chunk)) + len(str(element)) > max_length:
#             chunks.append(current_chunk)
#             current_chunk = BeautifulSoup("", 'html.parser')
#         current_chunk.append(element)
#
#     if len(current_chunk) > 0:
#         chunks.append(current_chunk)
#
#     return chunks
#
# # Разделяем HTML на части
# max_length = 300  # Максимальная длина для каждой части
# html_parts = split_html(html_content, max_length)
#
# # Выводим результат
# for i, part in enumerate(html_parts):
#     print(f"Часть {i + 1}:")
#     print(part)
#     print("------------------")
#





# html_str = soup.prettify()
#
# def insert_delimiters(text, length=300, delimiter="------------------"):
#     parts = [text[i:i+length] for i in range(0, len(text), length)]
#     return delimiter.join(parts)
#
# # Проверяем длину строки и вставляем разделители, если необходимо
# if len(html_str) > 300:
#     result_html = insert_delimiters(html_str)
# else:
#     result_html = html_str
#
# # Выводим результат
# print(result_html)


# Проверяем длину строки
# if len(html_str) > 300:
#     # Найдем позицию для вставки разделителя
#     split_index = 300
#
#     # Вставляем разделитель в указанную позицию
#     first_part = html_str[:split_index]
#     second_part = html_str[split_index:]
#
#     # Объединяем части с разделителем
#     result_html = first_part + "\n------------------\n" + second_part
# else:
#     result_html = html_str
#
# # Выводим результат
# print(result_html)
#
#







# Исходный HTML код
# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
# </head>
# <body>
#     <p>Stroka-----1--------</p>
#     <p>Stroka-----2-------</p>
#     <a>Stroka-----3--------</a>
#     <p>Stroka-----4--------</p>
#     <p>Stroka-----5--------</p>
#     <p>Stroka-----6--------</p>
#     <p>Stroka-----7--------</p>
#     <p>Stroka-----8--------</p>
#     <a>Stroka-----9--------</a>
#     <p>Stroka-----10--------</p>
#     <p>Stroka-----11--------</p>
#     <p>Stroka-----12--------</p>
#     <p>Stroka-----13--------</p>
#     <p>Stroka-----14--------</p>
#     <p>Stroka-----15--------</p>
#     <p>Stroka-----16--------</p>
# </body>
# </html>
# """
# print(len(html), '-=-=-=-=-=--=')
#
#
# def split_html(html, max_length=300):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     parts = []
#     current_part = ''
#     current_length = 0
#
#     for element in soup.recursiveChildGenerator():
#         element_str = str(element)
#
#         # Check if adding the next element would exceed max_length
#         if current_length + len(element_str) > max_length:
#             # Save the current part and reset
#             parts.append(current_part)
#             current_part = ''
#             current_length = 0
#
#         current_part += element_str
#         current_length += len(element_str)
#
#     # Append any remaining part
#     if current_part:
#         parts.append(current_part)
#
#     return parts

# def split_html(html, max_length=300):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     parts = []
#     current_part = ''
#
#     # Iterate over all elements in the soup object
#     for element in soup.recursiveChildGenerator():
#         if isinstance(element, str):
#             # Append string parts directly
#             current_part += element
#         else:
#             # Convert the tag or navigable string back to a string
#             current_part += str(element)
#
#         # Check if current part exceeds max_length
#         if len(current_part) >= max_length:
#             parts.append(current_part)
#             current_part = ''
#
#     # Append any remaining part
#     if current_part:
#         parts.append(current_part)
#
#     return parts

#
#
# parts = split_html(html)
#
# # Output the parts
# for i, part in enumerate(parts, 1):
#     print(f"Part {i}:\n{part}\n")
#


'''
(defr-html-py3.12) ~/Desktop/defr_html:feature/input_output ✗ python3 defr_html/main2.py
623 -=-=-=-=-=--=
Part 1:

html
<html lang="en">
<head>
</head>
<body>
<p>Stroka-----1--------</p>
<p>Stroka-----2-------</p>
<a>Stroka-----3--------</a>
<p>Stroka-----4--------</p>
<p>Stroka-----5--------</p>
<p>Stroka-----6--------</p>
<p>Stroka-----7--------</p>
<p>Stroka-----8--------</p>
<a>Stroka-----9--------</a>
<p>Stroka-----10--------</p>
<p>Stroka-----11--------</p>
<p>Stroka-----12--------</p>
<p>Stroka-----13--------</p>
<p>Stroka-----14--------</p>
<p>Stroka-----15--------</p>
<p>Stroka-----16--------</p>
<p>Stroka-----17--------</p>
</body>
</html>

Part 2:

<head>
</head>

<body>
<p>Stroka-----1--------</p>
<p>Stroka-----2-------</p>
<a>Stroka-----3--------</a>
<p>Stroka-----4--------</p>
<p>Stroka-----5--------</p>
<p>Stroka-----6--------</p>
<p>Stroka-----7--------</p>
<p>Stroka-----8--------</p>
<a>Stroka-----9--------</a>
<p>Stroka-----10--------</p>
<p>Stroka-----11--------</p>
<p>Stroka-----12--------</p>
<p>Stroka-----13--------</p>
<p>Stroka-----14--------</p>
<p>Stroka-----15--------</p>
<p>Stroka-----16--------</p>
<p>Stroka-----17--------</p>
</body>

Part 3:

<p>Stroka-----1--------</p>Stroka-----1--------
<p>Stroka-----2-------</p>Stroka-----2-------
<a>Stroka-----3--------</a>Stroka-----3--------
<p>Stroka-----4--------</p>Stroka-----4--------
<p>Stroka-----5--------</p>Stroka-----5--------
<p>Stroka-----6--------</p>Stroka-----6--------
<p>Stroka-----7--------</p>

Part 4:
Stroka-----7--------
<p>Stroka-----8--------</p>Stroka-----8--------
<a>Stroka-----9--------</a>Stroka-----9--------
<p>Stroka-----10--------</p>Stroka-----10--------
<p>Stroka-----11--------</p>Stroka-----11--------
<p>Stroka-----12--------</p>Stroka-----12--------
<p>Stroka-----13--------</p>Stroka-----13--------

Part 5:

<p>Stroka-----14--------</p>Stroka-----14--------
<p>Stroka-----15--------</p>Stroka-----15--------
<p>Stroka-----16--------</p>Stroka-----16--------
<p>Stroka-----17--------</p>Stroka-----17--------



'''



# MAX_LENGTH = 2000
#
# # Парсим HTML
# soup = BeautifulSoup(html, 'html.parser')
#
# # Создаем новые BeautifulSoup объекты для частей
# parts = []
# current_part = BeautifulSoup(features="html.parser")
# parts.append(current_part)
#
# current_length = 0
#
# # Итерация по элементам и распределение их по частям
# for element in soup.contents:
#     element_str = str(element)
#     element_length = len(element_str)
#
#     if current_length + element_length > MAX_LENGTH:
#         current_part = BeautifulSoup(features="html.parser")
#         parts.append(current_part)
#         current_length = 0
#
#     current_part.append(element)
#     current_length += element_length
#
# # Пишем результат в один файл с разделителем
# output_file = "output_files/output.html"
# with open(output_file, "w", encoding="utf-8") as file:
#     for i, part in enumerate(parts):
#         file.write(part.prettify())
#         if i < len(parts) - 1:
#             file.write("\n" + "-" * 50 + "\n")
#
# print(f"HTML разделен и сохранен в {output_file}")
#
#
#
#
#







# for element in soup:
#     element_str = str(element)
#     element_length = len(element_str)
#
#     if current_length + element_length > MAX_LENGTH:
#         parts.append(current_part)
#         current_part = element_str
#         current_length = element_length
#     else:
#         current_part += element_str
#         current_length += element_length
#
# # Не забудьте добавить последнюю часть
# if current_part:
#     parts.append(current_part)
#
# # Пишем результат в один файл с разделителем
# output_file = "output_files/output.html"
# with open(output_file, "w", encoding="utf-8") as file:
#     for i, part in enumerate(parts, 1):
#         file.write(f"-- fragment #{i}: {len(part)} chars --\n")
#         file.write(part)
#         if i < len(parts):
#             file.write("\n" + "-" * 50 + "\n")
#
# print(f"HTML разделен и сохранен в {output_file}")
#
#
#
#
#



# # Разбиваем HTML на части с учетом максимальной длины
# for element in soup.find_all(recursive=False):
#     element_str = str(element)
#     element_length = len(element_str)
#
#     # Если добавление текущего элемента приведет к превышению максимальной длины
#     if current_length + element_length > MAX_LENGTH:
#         parts.append(current_part)
#         current_part = element_str
#         current_length = element_length
#     else:
#         current_part += element_str
#         current_length += element_length
#
# # Не забудьте добавить последнюю часть
# if current_part:
#     parts.append(current_part)
#
# # Пишем результат в один файл с разделителем
# output_file = "output_files/output.html"
# with open(output_file, "w", encoding="utf-8") as file:
#     for i, part in enumerate(parts, 1):
#         file.write(f"-- fragment #{i}: {len(part)} chars --\n")
#         file.write(part)
#         if i < len(parts):
#             file.write("\n" + "-" * 50 + "\n")
#
# print(f"HTML разделен и сохранен в {output_file}")
#
#





































# # Итерация по элементам и распределение их по частям
# for element in soup:
#     element_str = str(element)
#     element_length = len(element_str)
#
#     if current_length + element_length > MAX_LENGTH:
#         parts.append(current_part)
#         current_part = element_str
#         current_length = element_length
#     else:
#         current_part += element_str
#         current_length += element_length
#
# # Не забудьте добавить последнюю часть
# if current_part:
#     parts.append(current_part)
#
# # Пишем результат в один файл с разделителем
# output_file = "output_files/output.html"
# with open(output_file, "w", encoding="utf-8") as file:
#     for i, part in enumerate(parts, 1):
#         file.write(f"-- fragment #{i}: {len(part)} chars --\n")
#         file.write(part)
#         if i < len(parts):
#             file.write("\n" + "-" * 50 + "\n")
#
# print(f"HTML разделен и сохранен в {output_file}")
#





# # Парсим HTML
# soup = BeautifulSoup(html, 'html.parser')
#
# # Получаем все элементы внутри <body>
# body_content = soup.body.contents
#
# # Определяем точку разбиения (половина элементов)
# split_point = len(body_content) // 2
#
# # Создаем списки для двух частей
# part1 = []
# part2 = []
#
# # Добавляем первую половину элементов в первую часть
# for element in body_content[:split_point]:
#     if isinstance(element, Tag):
#         part1.append(element)
#
# # Добавляем вторую половину элементов во вторую часть
# for element in body_content[split_point:]:
#     if isinstance(element, Tag):
#         part2.append(element)
#
# # Конвертируем части обратно в строки HTML
# part1_str = ''.join(str(tag) for tag in part1)
# part2_str = ''.join(str(tag) for tag in part2)
#
# print("HTML Part 1:")
# print(part1_str)
# print("\nHTML Part 2:")
# print(part2_str)
