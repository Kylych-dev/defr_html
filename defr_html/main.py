from typing import Generator
from bs4 import BeautifulSoup as bs
import re

# MAX_LENGTH = 4096
MAX_LENGTH = 20

CUR_LENGTH = 5717


def split_message(source: str, max_length: int =MAX_LENGTH) -> Generator[str, None, None]:
    """Splits the original message ('source') into fragments of 'max_length'."""
    with open(source, 'r') as file:
        data = file.read()


    print(len(data), '<------------------')


    # print(data.find('<a>'), '**********************************')
    data = '\n'.join(line for line in data.split('\n') if line.strip())

    # strong_tgs = (m.start() for m in re.finditer(r'<strong>', data))

    # print(strong_tgs, '**********************************')

    # a_tgs = re.findall(r'<a.*?>', data)

    # print(a_tgs, '**********************************')

    print('\n')
    print(len(data), '<------------------')


    # for strong in strong_tgs:
    #     print(strong, '**********************************')
    #     print(data[start:strong])
    #     print()
    #     print('-' * 50)
    #     print()
    #     yield data[start:strong]
    #     start = strong



    for i in range(0, len(data), max_length):
        yield data[i:i + max_length]







def split_message2(source, max_length=MAX_LENGTH):
    with open(source, 'r') as file:
        data = file.read()

    for i in range(0, len(data), max_length):
        yield data[i:i + max_length]

    # print(data)
    # yield data






if __name__ == '__main__':
    # res2 = split_message2('input_files/source.html')
    res2 = split_message2('input_files/sample.html')

    for fragment in res2:
        print(fragment)
        print()
        print('-' * 50)
        print()



    # res = split_message('input_files/source.html')
    # for fragment in res:
    #     print(fragment)
    #     print()
    #     print('-' * 50)
    #     print()



