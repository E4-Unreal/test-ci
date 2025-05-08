import os
from modules.unreal_plugin import UnrealPlugin

if __name__ == '__main__':
    new_plugin_name = os.environ['NEW_PLUGIN_NAME']
    unreal_plugin = UnrealPlugin()
    unreal_plugin.set_plugin_name(new_plugin_name)
