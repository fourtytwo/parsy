from parser import ConfigParser, FileParsert
import os
import shutil


def main():
    parsed_files = FileParsert()
    parsed_config = ConfigParser(parsed_files)
    create_directories(parsed_config)
    move_files(parsed_config , parsed_files)

def move_files(parsed_config , parsed_files):
    directory = os.getcwd()
    for dir , ext_list in parsed_config.config.items():
        for ext in ext_list:
            if ext in parsed_files.files:
                for file in parsed_files.files[ext]:
                    move_file_to(directory + os.path.sep + file , dir+os.path.sep+file)




def move_file_to(file_path , target):
    shutil.move(file_path , target)

def create_directories(config):
    for dir in config.config.keys():
        ensure_directory(dir)


def ensure_directory(dir):
    os.makedirs(dir , exist_ok=True)

if __name__ == '__main__':
    main()