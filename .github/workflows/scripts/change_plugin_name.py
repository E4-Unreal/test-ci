import os

from modules import unreal_plugin

if __name__ == '__main__':
    old_plugin_name = os.environ['OLD_PLUGIN_NAME']
    new_plugin_name = os.environ['NEW_PLUGIN_NAME']
    unreal_plugin.change_plugin_name(os.getcwd(), old_plugin_name, new_plugin_name)
