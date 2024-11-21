'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to list all the files in a directory

'''

from pathlib import Path


directory = Path('./')

files = [f for f in directory.iterdir() if f.is_file()]

print("Files in directory:", files)
