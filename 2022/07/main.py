import re

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory():
    def __init__(self, dir_name: str = None, parent_dir = None):
        self.dir_name = dir_name
        self.parent_dir = parent_dir
        self.sub_dirs = {}
        self.files = {}
        self.size = 0
    def __str__(self) -> str:
        return f"Name: {self.dir_name}\nSub Dirs: {self.sub_dirs}\nFiles: {self.files}\nSize: {self.size}"
    def make_sub_dir(self, sub_dir_name):
        sub_directory = Directory(sub_dir_name, self)
        self.sub_dirs[sub_dir_name] = sub_directory
    def add_file(self, file_name, file_size):
        new_file = File(file_name, file_size)
        self.files[file_name] = new_file
        self.size += new_file.size
    def recalc_dir_size(self):
        self.size = 0
        for file in self.files:
            self.size += file.size
        for dir in self.sub_dirs:
            self.size += dir.size
        # Would like to update all parents too. 
        

def cd_command(command: str, working_directory: Directory) -> Directory:
    new_directory_name = command.partition('cd')[2].strip()
    if new_directory_name == '..':
        new_directory = working_directory.parent_dir
    else:
        new_directory = working_directory.sub_dirs[new_directory_name]
    return new_directory

def build_dir_tree(terminal):
    home_dir = Directory('/', None)
    working_directory = home_dir
    for line in terminal:
        if line.strip('\n') == "$ cd /":
            working_directory = home_dir
        elif line.startswith("$ cd"):
            working_directory = cd_command(line, working_directory)
        elif line.startswith("dir"):
            sub_dir_name = line.partition('dir')[-1].strip()
            # Check if sub directory already exists
            if sub_dir_name not in working_directory.sub_dirs:
                working_directory.make_sub_dir(sub_dir_name)
        elif line[0].isdigit():
            # Then this is a file and we start with the size.
            file_size_str = re.search(r'\d+', line).group()
            file_name = line.partition(file_size_str)[-1].strip()
            if file_name not in working_directory.files:
                working_directory.add_file(file_name, int(file_size_str))
        if not isinstance(working_directory, Directory):
            raise TypeError(f"{working_directory} is not a Directory\nJust processed line:{line}")
    return home_dir

if __name__ == "__main__":
    working_directory = ''
    with open('test-data.txt', 'r') as file:
        terminal = file.readlines()
    # Will always start with a home directory
    home_dir = build_dir_tree(terminal)
    

    