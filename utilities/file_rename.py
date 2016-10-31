import os
import re


def rename_files(dir_path, pattern, replacement):
    cwd = os.chdir(dir_path)
    file_list = os.listdir(dir_path)
    new_file_list = []
    for fl in file_list:
        print('change {} name'.format(fl))
        new_fl = re.sub(pat, replacement, fl)
        new_file_list.append(new_fl)
        os.rename(fl, new_fl)  # rename file
        print('New File Name: {:<30}'.format(new_fl))
    print(new_file_list)

path = '/home/beenorgone/Desktop/Thao English/New Market Leader Elementary Audio CD'
pat = r'([\w])market_leader-elementary-([\w+])'
rep = r'market_leader-elementary-\2'

rename_files(path, pat, rep)
