import os
import sys
import chardet

def replace_text(file_path: str, text_tuple: tuple[str, str]):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            line = line.replace(text_tuple[0], text_tuple[1])
            f.write(line)

def replace_texts(file_path: str, text_tuples: list[tuple[str, str]]):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            for text_tuple in text_tuples:
                line = line.replace(text_tuple[0], text_tuple[1])
            f.write(line)

class UnrealPlugin:
    def __init__(self, plugin_directory = os.getcwd()):
        self.extension = '.uplugin'
        self.path = ''
        self.name = ''
        self.readme_path = 'README.md'

        # 작업 폴더 변경
        if os.path.isdir(plugin_directory):
            os.chdir(plugin_directory)
        else:
            sys.exit(plugin_directory + ' is not exist')

        # 플러그인 파일명 불러오기
        file_list = os.listdir()
        plugin_file_list = [file for file in file_list if file.endswith(self.extension)]
        if plugin_file_list:
            self.path = plugin_file_list[0]
            self.name = plugin_file_list[0].replace(self.extension, '')
        else:
            sys.exit('Plugin file is not found')

    def set_name(self, new_name):
        # 새로운 플러그인 이름 유효성 검사
        if new_name is None:
            sys.exit('Plugin name is None')
        elif self.name == new_name:
            sys.exit('Plugin name is same')

        # 변수 선언
        plugin_name_tuple = (self.name, new_name)
        new_plugin_path = new_name + self.extension

        # 플러그인 파일 수정
        replace_text(self.path, plugin_name_tuple)
        os.rename(self.path, new_plugin_path)

        # README 파일 수정
        replace_text(self.readme_path, plugin_name_tuple)
