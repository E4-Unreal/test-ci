import os
import sys

def check_plugin_name(old_plugin_name, new_plugin_name):
    if old_plugin_name is None or new_plugin_name is None
        sys.exit('Plugin name is None')
    elif old_plugin_name == new_plugin_name
        sys.exit('Plugin name is same')

def change_plugin_name(old_plugin_name, new_plugin_name):
    check_plugin_name(old_plugin_name, new_plugin_name)
    
    plugin_file_path = old_plugin_name + '.uplugin'

    with open(plugin_file_path, 'r+') as f:
        lines = f.readlines()
    for line in lines:
        line = line.replace(old_plugin_name, new_plugin_name)
        f.write(line)
        
if __name__ == '__main__':
    old_plugin_name = os.environ.get('OLD_PLUGIN_NAME')
    new_plugin_name = os.environ.get('NEW_PLUGIN_NAME')

    change_plugin_name(old_plugin_name, new_plugin_name)