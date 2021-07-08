from tags import Tags
import os


class Compile(object):
    def __init__(self, file_path: str) -> None:
        self.parse(file_path)
        try:
            self.create_html_file(self.new_filename)
        except AttributeError:
            return None

    @staticmethod
    def get_indexes_substrings(string: str, *substrings) -> dict:
        if not isinstance(string, str):
            raise TypeError('1-й аргумент функции должен быть строковым объектом')

        result = {}

        for index in range(len(string)):
            if string[index] in substrings:
                result.setdefault(string[index], []).append(index)

        return result

    def parse(self, file_path: str) -> None:
        if not file_path.endswith('.txt'):
            print('Нужно указать файл с расширением .txt')
            return None

        self.new_filename = f'{file_path[:-4:]}.html' 

        try:
            with open(f'txt files/{file_path}', 'r', encoding='utf-8') as txt_file:
                self.text = ''
                for string in txt_file:
                    tag_indexes = self.get_indexes_substrings(string, '<', '>')
                    start_tag = tag_indexes.get('<')
                    end_tag = tag_indexes.get('>')
                    all_tags = tuple(zip(start_tag, end_tag))

                    new_str = string
                    
                    for i, j in reversed(all_tags):
                        for tag in Tags.main:
                            if tag in new_str:
                                new_str = new_str[:i:] + new_str[i:j + 1:].replace(tag, Tags.main[tag]) + new_str[j + 1::]

                    self.text += new_str

        except FileNotFoundError:
            print('файл не найден')
            self.new_filename = None
            return None

    def create_html_file(self, filename: str) -> None:
        if filename is None:
            return None
        with open(f'finished files/{filename}', 'w', encoding='utf-8') as new_file:
            new_file.write(self.text)
