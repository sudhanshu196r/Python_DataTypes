'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to list all the files in a directory

'''

import os

def main():
    
    user_profile = os.getenv('USERPROFILE')  # Windows user home directory


    path_variable = os.getenv('PATH')

    
    custom_var = os.getenv('MY_CUSTOM_VAR', 'Default Value')

   
    print(f"User Profile Directory: {user_profile}")
    print(f"PATH: {path_variable}")
    print(f"Custom Variable: {custom_var}")

if __name__ == "__main__":
    main()
