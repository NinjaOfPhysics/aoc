from typing import NewType

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory():
    def __init__(self, dir_name: str, parent_dir = None):
        self.dir_name = dir_name
        self.parent_dir = parent_dir
        self.sub_dirs = {}
        self.files = {}
        self.size = 0
    def make_sub_dir(self, sub_dir_name):
        sub_directory = Directory(sub_dir_name, self.dir_name)
        self.sub_dirs[sub_dir_name] = sub_directory
    def add_file(self, file_name, file_size):
        new_file = File(file_name, file_size)
        self.files[file_name] = new_file
        self.size += new_file.size
    def recalc_dir_size(self):
        self.size = 0
        for file in self.files:
            self.size += file.size

def cd_command(command: str, working_directory: Directory) -> Directory:
    new_directory_name = command.partition('cd')[2].strip()
    if new_directory_name == '..':
        new_directory = working_directory.parent_dir
    else:
        new_directory = working_directory.sub_dirs[new_directory_name]
    return new_directory

if __name__ == "__main__":
    working_directory = ''
    with open('test-data.txt', 'r') as file:
        terminal = file.readlines()
    # Will always start with a home directory
    home_dir = Directory('/', None)
    working_directory = home_dir
    for line in terminal:
        if line.startswith("$ cd"):
            working_directory = cd_command(line, working_directory)
        elif line.startswith("dir"):
            sub_dir_name = line.partition('dir').strip()
            sub_dir = Directory(sub_dir_name, working_directory)
            
