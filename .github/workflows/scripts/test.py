import os

repository_name = os.environ.get("GITHUB_REPOSITORY")
print(repository_name.split('/')[1])