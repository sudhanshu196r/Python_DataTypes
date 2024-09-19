'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to list all the files in a directory

'''

import os

def main():
    username = os.getenv('USERNAME')  # Works on Windows
    
    print(f"Current Username: {username}")

if __name__ == "__main__":
    main()
