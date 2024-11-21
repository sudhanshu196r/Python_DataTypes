'''

    @Author: Sudhanshu Kumar
    @Date: 18-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 18-09-2024
    @Title : Write a Python program print inbuilt functions desc and syntax

'''

def main():
    func = input("Enter function name : ")
    help(eval(func))

if __name__=="__main__":
    main()