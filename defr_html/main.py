from typing import Generator
from bs4 import BeautifulSoup as bs
import re
import click





# MAX_LENGTH = 4096
MAX_LENGTH = 500

CUR_LENGTH = 5717


def split_message(source: str, max_length: int =MAX_LENGTH) -> Generator[str, None, None]:
    """Splits the original message ('source') into fragments of 'max_length'."""
    with open(source, 'r') as file:
        data = file.read()


    data = '\n'.join(line for line in data.split('\n') if line.strip())

    for i in range(0, len(data), max_length):
        yield data[i:i + max_length]


# @click.command()
# @click.option('--source', '-s', help='Path to the source file')
# @click.argument('source', type=click.Path(exists=True))
def split_message2(source, max_length=500):
    with open(source, 'r', encoding='utf-8') as file:
        # data = file.read()
        content = file.read()
    # content = data.

    for i in range(0, len(content), max_length):
        yield content[i:i + max_length]


if __name__ == '__main__':
    res2 = split_message2('input_files/sample.html')
    # res2 = split_message2()
    for num, fragment in enumerate(res2, 1):
        print(num, fragment)
        print()
        print('-' * 50)
        print()








'''
import click 

@click.command()
@click.option('--name', '-n', default='Bob', help='First_name')
def main(name):
    print(f'Hello, {name}!')
    
if __name__ == '__main__':
    main()



>>> python main.py --name Alice
    ... Hello, Alice!

>>> python main.py --help
Usage: main.py [OPTIONS]
options:
  -n, --name TEXT  First_name
  --help       Show this message and exit.
'''


