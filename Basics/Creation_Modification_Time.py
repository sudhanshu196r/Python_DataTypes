'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to get absolute path

'''


import os
import datetime

def get_file_times(file_path):

    """
    Description: 
        This method gets the file creation time and modification time
    Parameters:
        file_path: Represents the path
    Returns:
        It returns the creation and modification time

    """
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)
    
    # Convert timestamps to readable datetime format
    creation_date = datetime.datetime.fromtimestamp(creation_time)
    modification_date = datetime.datetime.fromtimestamp(modification_time)
    
    return creation_date, modification_date

def main():

    file_path = 'Basics/CurrentUser.py' 
    
    creation_date, modification_date = get_file_times(file_path)
    
    print(f"Creation Time: {creation_date}")
    print(f"Modification Time: {modification_date}")

if __name__ == "__main__":
    main()
