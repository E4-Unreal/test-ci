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
        self.path: str = None
        self.name: str = None
        self.readme_path = os.path.join(self.plugin_directory, 'README.md')
        self.all_file_paths = []
        self.header_file_paths = []

        # 작업 폴더 변경
        if os.path.isdir(self.plugin_directory):
            os.chdir(self.plugin_directory)
        else:
            sys.exit(self.plugin_directory + ' is not exist')

        # 플러그인 파일 경로 및 이름 불러오기
        plugin_paths = glob.glob(os.path.join(self.plugin_directory, '*' + self.extension))
        if plugin_paths:
            self.path = plugin_paths[0]
            self.name = os.path.basename(self.path).replace(self.extension, '')
        else:
            sys.exit('Plugin file is not found')

        # 모든 파일 경로 불러오기
        all_file_paths = glob.glob(os.path.join(self.plugin_directory, 'Source', self.name, '**', '*.*'), recursive=True)
        for file_path in all_file_paths:
            if file_path.endswith('.h') or file_path.endswith('.cpp') or file_path.endswith('.cs'):
                self.all_file_paths.append(file_path)
        self.all_file_paths.append(self.path)
        self.all_file_paths.append(self.readme_path)

        # 모든 헤더 파일 경로 불러오기
        self.header_file_paths = [file_path for file_path in self.all_file_paths if file_path.endswith('.h')]

    def set_name(self, new_name):
        # 새로운 플러그인 이름 유효성 검사
        if new_name is None:
            sys.exit('Plugin name is None')
        elif self.name == new_name:
            sys.exit('Plugin name is same')

        # 모든 파일 수정
        for file_path in self.all_file_paths:
            replace_text(file_path, (self.name, new_name))

        # 모든 헤더 파일 수정
        text_tuples = [
            (self.name + '_API', new_name.upper() + '_API'),
            (self.name.upper() + '_API', new_name.upper() + '_API')
        ]
        for header_file_path in self.header_file_paths:
            replace_texts(header_file_path, text_tuples)

        # 모든 파일명 수정
        for file_path in self.all_file_paths:
            dirname = os.path.dirname(file_path)
            basename = os.path.basename(file_path)
            if self.name in basename:
                os.rename(file_path, os.path.join(dirname, basename.replace(self.name, new_name)))
