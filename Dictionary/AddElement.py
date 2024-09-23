'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to create an array and print the array

'''

def addElement(my_dict):
    key = input("Key : ")
    value = input(" Value : ")
    my_dict[key] = value
    return my_dict

def createDict():
    my_dict = {}
    n = int(input("Enter size of dictionary : "))
    for i in range(n):
        key = input("Key : ")
        value = input("Value : ")
        my_dict[key]=value

    return my_dict


def main():
    my_dict = createDict()
    print(my_dict)
    print("Enter key value pair to add : ")
    addElement(my_dict)
    print(my_dict)

if __name__=="__main__":
    main()