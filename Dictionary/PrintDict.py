'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to print dictionary using loop

'''

def printDict(my_dict):
    """
    Description:
        Print Dictionary using loops
    Parameters:
        Takes a dictionary as parameter
    Returns: 

    """
    print("Printing only Key: ")
    for key in my_dict:
        print(key)

    print("Printing only values: ")
    for value in my_dict.values():
        print(value)

    print("Key :     Value : ")
    for key,value in my_dict.items():
        print(f"{key}         {value}")

def main():
    my_dict = {1:'Apple', 2:'Mango', 3:'Banana'}
    printDict(my_dict)

if __name__=="__main__":
    main()

    