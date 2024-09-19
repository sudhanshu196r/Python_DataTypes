'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to execute external command

'''

import os


cpu_count = os.cpu_count()

print(f"Number of CPUs: {cpu_count}")
