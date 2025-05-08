import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.unreal_plugin import UnrealPlugin

if __name__ == '__main__':
    new_plugin_name = os.environ['NEW_PLUGIN_NAME']
    unreal_plugin = UnrealPlugin()
    unreal_plugin.set_name(new_plugin_name)
