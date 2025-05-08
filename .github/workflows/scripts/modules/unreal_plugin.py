import os
import sys
import glob

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
        self.plugin_directory = plugin_directory
        self.extension = '.uplugin'
        self.path = ''
        self.name = ''
        self.readme_path = 'README.md'
        self.header_file_paths = []
        self.cpp_file_paths = []

        # 작업 폴더 변경
        if os.path.isdir(self.plugin_directory):
            os.chdir(self.plugin_directory)
        else:
            sys.exit(self.plugin_directory + ' is not exist')

        # 플러그인 파일명 불러오기
        file_list = os.listdir()
        plugin_file_list = [file for file in file_list if file.endswith(self.extension)]
        if plugin_file_list:
            self.path = plugin_file_list[0]
            self.name = plugin_file_list[0].replace(self.extension, '')
        else:
            sys.exit('Plugin file is not found')

        # 모든 헤더 파일 경로 불러오기
        self.header_file_paths = glob.glob(os.path.join(self.plugin_directory, 'Source', self.name, '**', '*.h'), recursive=True)

        # 모든 cpp 파일 경로 불러오기
        self.cpp_file_paths = glob.glob(os.path.join(self.plugin_directory, 'Source', self.name, '**', '*.cpp'), recursive=True)

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

        # 모든 헤더 파일 수정
        text_tuples = [
            plugin_name_tuple,
            (self.name + '_API', new_name.upper() + '_API'),
            (self.name.upper() + '_API', new_name.upper() + '_API')
        ]
        for header_file_path in self.header_file_paths:
            replace_texts(header_file_path, text_tuples)

        # 모든 cpp 파일 수정
        for cpp_file_path in self.cpp_file_paths:
            replace_text(cpp_file_path, plugin_name_tuple)
