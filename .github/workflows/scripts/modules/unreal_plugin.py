import os
import sys

def change_plugin_name(plugin_directory, old_plugin_name, new_plugin_name):
    # 작업 폴더 변경
    if os.path.isdir(plugin_directory):
        os.chdir(plugin_directory)
    else:
        sys.exit(plugin_directory + ' is not exist')

    # 플러그인 이름 검사
    if old_plugin_name is None or new_plugin_name is None:
        sys.exit('Plugin name is None')
    elif old_plugin_name == new_plugin_name:
        sys.exit('Plugin name is same')

    # 플러그인 파일 확인
    plugin_file_path = old_plugin_name + '.uplugin'
    if not os.path.isfile(plugin_file_path):
        sys.exit(plugin_file_path + ' is not exist')

    # 플러그인 이름 수정
    with open(plugin_file_path, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            line = line.replace(old_plugin_name, new_plugin_name)
            f.write(line)
