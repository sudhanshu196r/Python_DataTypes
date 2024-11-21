'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to remove a key from the dictionary

'''

def removeKey(my_dict):
    """
    Description:
        This function removes a key
    Parameters:
        my_dict: Represents the dictionary on which operation is to be performed
    Returns:
        Returns the final dictionary
    """
    my_dict.pop(1)
    return my_dict

def main():
    my_dict = {1:"Apple", 2:"Mango", 3:"Banana"}
    print(removeKey(my_dict))

if __name__=="__main__":
    main()