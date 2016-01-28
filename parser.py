import os

class ConfigParser(object):
    def __init__(self, files ,cfg_file='config.par'):
        self.input_file = cfg_file
        self.config = self.load_config(cfg_file, files)

    def load_config(self , input, files):
        res_dict = {}
        try:
            with open(input  , 'r' , encoding='utf-8') as fh:
                for line in fh:
                    if line.lstrip().startswith("#") or line.isspace():
                        continue
                    split_str = line.split(':')
                    dir = os.getcwd()+ os.path.sep + split_str[0].strip()
                    extensions = (' '.join(split_str[1].split())).split(' ')
                    for ex in extensions:
                        if ex in files.files:
                            res_dict[dir] = extensions
                            break
        except:
            print("An error occured while reading the config file, default will be loaded")

        return res_dict


class FileParsert(object):
    def __init__(self):
        self.files = self.load_files()

    def load_files(self):
        res_dict = {}
        for file in  os.listdir(os.getcwd()):
            name , extension = os.path.splitext(file)
            extension = extension[1:]
            if extension not in res_dict:
                res_dict[extension] = [file]
            else:
                res_dict[extension].append(file)

        return res_dict
