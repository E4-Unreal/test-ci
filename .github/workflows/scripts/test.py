import os

old_plugin_name = os.environ.get("OLD_PLUGIN_NAME")
new_plugin_name = os.environ.get("NEW_PLUGIN_NAME")

print(f'Old Plugin Name: {old_plugin_name}')
print(f'New Plugin Name: {new_plugin_name}')