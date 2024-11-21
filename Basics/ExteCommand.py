'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to execute external command

'''

import subprocess

def main():
    command = [input()]
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Print the output
    print("Command output:")
    print(result.stdout)

if __name__=="__main__":
    main()
