from typing import Generator
import re

MAX_LENGTH = 4096

CUR_LENGTH = 5717


def split_message(source: str, max_length: int =MAX_LENGTH) -> Generator[str, None, None]:
    """Splits the original message ('source') into fragments of 'max_length'."""
    with open(source, 'r') as file:
        data = file.read()


    print(len(data), '<------------------')


    # print(data.find('<a>'), '**********************************')
    # data = '\n'.join(line for line in data.split('\n') if line.strip())

    a_tgs = re.findall(r'<a.*?>', data)

    print(a_tgs, '**********************************')

    print('\n')
    print(len(data), '<------------------')



    for i in range(0, len(data), max_length):
        yield data[i:i + max_length]


if __name__ == '__main__':
    res = split_message('input_files/source.html')
    for fragment in res:
        print(fragment)
        print()
        print('-' * 50)
        print()



