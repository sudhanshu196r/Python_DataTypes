'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to get absolute path

'''


import os

def get_absolute_path(file_path):
    """
    Description: 
        This method converts file path to absolute path
    Parameters:
        file_path: Represents the relative path
    Returns:
        It returns the absolute path

    """


    abs_path = os.path.abspath(file_path)
    return abs_path

def main():
    
    relative_path = 'CurrentUser.py'

    absolute_path = get_absolute_path(relative_path)
    
    print(f"Absolute Path: {absolute_path}")

if __name__ == "__main__":
    main()
