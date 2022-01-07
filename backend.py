import os
import win32api
from log_file import Logging


class Files:
    """
    Currently for windows only
    Can only merge txt files for now
    """

    def __init__(self, file_name_to_search, file_ext_to_search, file_name_to_save, dir_to_save, dir_to_search='root'):
        self.drives = None
        self.file_name_to_search = file_name_to_search
        self.file_ext_to_search = file_ext_to_search
        self.file_name_to_save = file_name_to_save
        self.dir_to_save = dir_to_save
        self.file_path_list = []
        self.dir_to_search = dir_to_search
        self.lg = Logging(os.getcwd() + '\\' + 'logs.txt')

    def get_drives(self):
        """This function gets all the drives in computer"""
        print("Drives getting in progress....")
        self.drives = win32api.GetLogicalDriveStrings()
        self.drives = self.drives.split('\000')[:-1]
        print("Drives getting DONE")

    def scan_path(self, path):
        try:
            os.chdir(path)
            curr_files = os.listdir()
        except Exception as e:
            self.lg.error(e)
            return
        for file in curr_files:
            if '.' in file:
                file_name = file.split('.')[0]
                ext_name = file.split('.')[1]
                if file_name.lower().find(
                        self.file_name_to_search.lower()) > -1 and ext_name == self.file_ext_to_search:
                    self.file_path_list.append(path + file)
            else:
                self.scan_path(path + '{}\\'.format(file))

    def get_paths(self):
        print('getting paths..')
        if self.dir_to_search == 'root':
            self.get_drives()
            for i in self.drives:
                self.scan_path(i)
        else:
            self.scan_path(self.dir_to_search)
        print('paths getting done')

    def merge_and_save(self):
        print('merging...')
        file_to_save = open(self.dir_to_save + self.file_name_to_save + '.txt', 'w+')
        for file_path in self.file_path_list:
            try:
                f = open(file_path, 'r')
                file_to_save.write(f.read() + '\n')
                f.close()
            except Exception as e:
                self.lg.error(e)
        print('merging done')

    def run_it(self):
        self.get_paths()
        self.merge_and_save()
