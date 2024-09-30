'''

    @Author: Sudhanshu Kumar
    @Date: 30-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 30-09-2024
    @Title : Python program to reverse a string

'''

def reverseString(string):
    rev_str=''
    for chr in string:
        rev_str = chr+rev_str
    return rev_str

def main():
    string = 'hello'
    print(reverseString(string))

if __name__=="__main__":
    main()