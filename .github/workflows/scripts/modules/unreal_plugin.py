import os
import sys

def replace_text(file_path, old_text, new_text):
    with open(file_path, 'r+', encoding='UTF8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            line = line.replace(old_text, new_text)
            f.write(line)

class UnrealPlugin:
    def __init__(self, plugin_directory = os.getcwd()):
        self.extension = '.uplugin'
        self.plugin_path = ''
        self.plugin_name = ''
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
            self.plugin_path = plugin_file_list[0]
            self.plugin_name = plugin_file_list[0].replace(self.extension, '')
        else:
            sys.exit('Plugin file is not found')

    def set_plugin_name(self, new_plugin_name):
        # 새로운 플러그인 이름 유효성 검사
        if new_plugin_name is None:
            sys.exit('Plugin name is None')
        elif self.plugin_name == new_plugin_name:
            sys.exit('Plugin name is same')

        # 플러그인 파일 수정
        replace_text(self.plugin_path, self.plugin_name, new_plugin_name)
        new_plugin_path = new_plugin_name + self.extension
        os.rename(self.plugin_path, new_plugin_path)

        # README 파일 수정
        replace_text(self.readme_path, self.plugin_name, new_plugin_name)
