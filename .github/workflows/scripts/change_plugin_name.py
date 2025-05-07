import os

def change_plugin_name():
    old_plugin_name = os.environ.get('OLD_PLUGIN_NAME')
    new_plugin_name = os.environ.get('NEW_PLUGIN_NAME')

    plugin_file_path = old_plugin_name + '.uplugin'

    with open(plugin_file_path, 'r+') as f:
        lines = f.readlines()
    for line in lines:
        line = line.replace(old_plugin_name, new_plugin_name)
        f.write(line)
        
if __name__ == '__main__':
    change_plugin_name()