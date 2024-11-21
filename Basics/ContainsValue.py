'''

    @Author: Sudhanshu Kumar
    @Date: 18-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 18-09-2024
    @Title : Write a Python program to check if a particular value is present inside a list

'''

def main():
    string_list = input("Enter comma seprated integers: ")
    list1 = string_list.split(",")
    val = input("enter value to check: ")
    if val in list1:
        print("True")
    else:
        print("False")


if __name__=="__main__":
    main()
