from typing import Generator
from bs4 import BeautifulSoup as bs
import re
import click



MAX_LENGTH = 4096
# MAX_LENGTH = 5



# @click.command()
# @click.option('--source', '-s', help='Path to the source file')
# @click.argument('source', type=click.Path(exists=True))
def split_message(source: str, max_length=MAX_LENGTH) -> Generator[str, None, None]:
    """Splits the original message (`source`) into fragments of the specified length
        (`max_len`)."""
    with open(source, 'r', encoding='utf-8') as file:
        html_content = file.read()
        soup = bs(html_content, 'html5lib')
        # html_content = soup.prettify()

        html_content = str(soup)

        print(len(html_content))

        liness = '-' * 50

        fragment_number, current_length = 1, 0
        fragments, tag_stack = [], []
        current_fragment = ''

        for char in html_content:
            current_fragment += char
            current_length += 1

            if char == '<':
                tag_stack.append(current_length)
            elif char == '>':
                tag_stack.pop()

            if current_length >= max_length and not tag_stack:
                fragments.append(current_fragment)
                current_fragment = ''
                current_length = 0
                fragment_number += 1

        if current_fragment:
            fragments.append(current_fragment)

        for i, fragment in enumerate(fragments):
            yield fragment
            if i < len(fragments) - 1:
                yield f'{liness} fragment №{fragment_number}: {len(fragment)} chars {liness}'
                fragment_number += 1


if __name__ == '__main__':
    res2 = split_message('input_files/sample.html')
    with open('output_files/sample.html', 'w', encoding='utf-8') as file:
        for part in res2:
            file.write(part + '\n')
