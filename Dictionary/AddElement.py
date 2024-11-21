'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to create an array and print the array

'''

def addElement(my_dict):
    """
    Description:
        It add new key value pair to the dictionary
    Parameters:
        my_dict: Takes an existing dictionary as an argument
    Returns: 
        returns dict after adding key value pair
    """
    key = input("Key : ")
    value = input(" Value : ")
    my_dict[key] = value
    return my_dict

def createDict():
    """
    Description:
        This function creates a dictionary
    Parameters:
    
    Returns: 
        returns a dictionary
    """
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