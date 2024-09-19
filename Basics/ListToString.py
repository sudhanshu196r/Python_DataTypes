'''

    @Author: Sudhanshu Kumar
    @Date: 18-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 18-09-2024
    @Title : Write a Python program to check convert a list to string

'''

def list_String(list1):
    ans = ",".join(list1)
    return ans

def main():
    list1 = []
    length = int(input("Enter length for list"))
    for x in range(0,length):
        list1.append(input())
    print(list1)
    print(list_String(list1))

if __name__=="__main__":
    main()
